import requests
import json
from .helpers import *

def notify_slack(webhook, report):
    n = 20 # slack asks that each request have no more than 20 attachments
    if len(report) <= n:
        r = requests.post(webhook, json={'text': "", 'attachments': report})
        if r.status_code != 200:
            print(r.status_code)
            print(r.json())
    else:
        multiple_requests = [report[i:i + n] for i in range(0, len(report), n)]
        for req in multiple_requests:
            r = requests.post(webhook, json={'text': "", 'attachments': req})
            if r.status_code != 200:
                print(r.status_code)
                print(r.json())

def get_formatted_versions(version_used):
    version_names = []
    for v in version_used:
        version_names.append(v['version'] + " in " + v['file'])
    return '\n'.join(version_names)

def is_new(date):
    return within_last_sprint(date)

def get_color(vulnerability):
    if is_new(vulnerability['publish_date']):
        return 'danger'
    else:
        return 'warning'

def get_attachment_text(vulnerability):
    description = vulnerability['description']
    urgent = ""
    if is_new(vulnerability['publish_date']):
        urgent = "NEW!"
    parts = [
        urgent,
        "",
        "",
        "",
        "",
        "ID: " + vulnerability["id"],
        "Published: " + date_string(vulnerability['publish_date'])
    ]
    if description:
        parts.append(
            description
        )
    return '\n'.join(parts)

def formatVulnerabilities(vulnerabilities, dep_info):
    attachments = []
    for v in vulnerabilities:
        title = "{0} - {1}".format(dep_info['name'], v['summary'])
        unaffected = v['unaffected_versions']
        if not unaffected:
            unaffected = 'None'
        if 'link' not in v:
            v['link'] = None
        attach = {
            "fallback": title,
            "color": get_color(v),
            "title": title,
            "title_link": v['link'],
            "text": get_attachment_text(v),
            "fields": [
                {
                    "title": "Our Versions",
                    "value": get_formatted_versions(dep_info['version'])
                },
                {
                    "title": "Patched Versions",
                    "value": v['patched_versions'],
                    "short": True
                },
                {
                    "title": "Unaffected Versions",
                    "value": unaffected,
                    "short": True
                }
            ],
            "ts": dep_info['updated']
        }
        attachments.append(attach)
    return attachments


def generate_security_report(response):
    vulnerable = []
    for d in response['dependencies']:
        dep = response['dependencies'][d]
        if dep['vulnerabilities']:
            dep_info = {
                'name': dep['name'],
                'version': dep['version_used'],
                'updated': response['scan_time']
            }
            vulnerable.extend(formatVulnerabilities(dep['vulnerabilities'], dep_info))
    return vulnerable

def batch_by_outdatedness(dependencies):
    severity = {
        'minor': {
            'dependencies': [],
            'color': "#ffb74d",
            'desc': 'a minor update available'
        },
        'middle': {
            'dependencies': [],
            'color': "#f57c00",
            'desc': 'an update available'
        },
        'major': {
            'dependencies': [],
            'color': "#d84315",
            'desc': 'a major update available'
        }
    }
    for d in dependencies:
        avail = d['version_available']
        if not avail:
            continue
        for version in d['version_used']:
            v = dict(version)
            v['available'] = avail
            v['dependency'] = d['name']
            if major_release(version['version'], avail):
                severity['major']['dependencies'].append(v)
            elif minor_release(version['version'], avail):
                severity['minor']['dependencies'].append(v)
            elif other_release(version['version'], avail):
                severity['middle']['dependencies'].append(v)
    return severity

def get_version_text(dependencies):
    ds = []
    for d in dependencies:
        ds.append("*{0}* in {1}: {2} => {3}.".format(d['dependency'], d['file'], d['version'], d['available']))
    string = '\n'.join(ds)
    return string

'''
Create attachment for outdated versions of a particular group
If more than n members in this group,
breaks into separate attachments so the slack text doesn't get cut off
'''
def format_version_attachment(group, ts):
    n = 80
    tolerance = 5
    if len(group['dependencies']) <= n:
        groups = [group['dependencies']]
    else:
        groups = [group['dependencies'][i:i + n] for i in range(0, len(group['dependencies']), n)]
    if len(groups[-1]) < tolerance and len(groups) > 1: # avoid super small groups
        groups[-2].extend(groups[-1])
        groups = groups[:-1]
    attachments = []
    for g in groups:
        title_text = "{0} dependencies have {1}.".format(len(g), group['desc'])
        attach = {
            "fallback": title_text,
            "color": group['color'],
            "title": title_text,
            "text": get_version_text(g),
            "mrkdwn_in": ["text"],
            "ts": ts
        }
        attachments.append(attach)
    return attachments

def generate_versions_report(response):
    grouped = batch_by_outdatedness(response['dependencies'].values())
    attachments = []
    for g in grouped:
        attachments.extend(format_version_attachment(grouped[g], response['scan_time']))
    return attachments

def generate_all_reports(response):
    attachments = []
    attachments.extend(generate_security_report(response))
    attachments.extend(generate_versions_report(response))
    return attachments

notify_methods = {
    'slack': notify_slack
}

notify_types = {
    'all': generate_all_reports,
    'updates': generate_versions_report,
    'vulnerabilities': generate_security_report
}

def notify(params, response, notification_method='slack', notification_type='all'):
    formatted_report = notify_types[notification_type](response)
    send_report = notify_methods[notification_method](params["webhook"], formatted_report)

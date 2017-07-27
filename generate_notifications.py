import requests
import json
import datetime
from helpers import convert_versioneye_timestamp as get_time
from sample_data import report as test_report

def notifySlack(params, report):
    r = requests.post(params['slack_webhook'], json={'text': "", 'attachments': report})
    print(r.status_code)


def notifyEmail(report):
    pass

def notifyAll(report):
    notifySlack(formattedReport)
    notifyEmail(formattedReport)

security_keys = [
    'id',
    'name',
    'sv_count',
    'updated_at',
    'dependencies'
]

def getFormattedVersions(version_used):
    version_names = []
    for v in version_used:
        version_names.append(v['version'] + " in " + v['file'])
    return '\n'.join(version_names)

def date_string(seconds):
    t = datetime.datetime.fromtimestamp(seconds)
    return t.strftime("%m-%d-%Y")

def getAttachmentText(vulnerability):
    description = vulnerability['description']
    parts = [
        "",
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
            "color": "danger",
            "title": title,
            "title_link": v['link'],
            "text": getAttachmentText(v),
            "fields": [
                {
                    "title": "Our Versions",
                    "value": getFormattedVersions(dep_info['version'])
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


def generateSecurityReport(response):
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

def generateVersionsReport(response):
    pass

def generateAllReports(response):
    security = generateSecurityReport(response)
    versions = generateVersionsReport(response)
    # TODO combine

notify_methods = {
    'slack': notifySlack,
    'email': notifyEmail,
    'all': notifyAll
}

notify_types = {
    'all': generateAllReports,
    'updates': generateVersionsReport,
    'vulnerabilities': generateSecurityReport
}

def notify(params, response, notification_method='slack', notification_type='vulnerabilities'):
    formatted_report = notify_types[notification_type](response)
    send_report = notify_methods[notification_method](params, formatted_report)

# sec_report = generateSecurityReport(test_report)
# notifySlack({'slack_webhook': "https://hooks.slack.com/services/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"}, sec_report)

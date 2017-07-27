import requests
import json
from datetime import datetime
import time, pytz, tzlocal
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

def back_to_ts(time_string):
    date_template = "%Y-%m-%dT%H:%M:%S"
    time_string = time_string.split('.')[0]

    local_timezone = tzlocal.get_localzone()
    utc_time = datetime.strptime(time_string, date_template)
    local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
    return time.mktime(local_time.timetuple())

def formatVulnerabilities(vulnerabilities, dep_info):
    attachments = []
    for v in vulnerabilities:
        title = "Dependency {0} has a security vulnerability.".format(dep_info['name'])
        unaffected = v['unaffected_versions_string']
        if not unaffected:
            unaffected = 'None'
        attach = {
            "fallback": title,
            "color": "danger",
            "title": title,
            "title_link": v['links'][list(v['links'])[0]],
            "text": v['description'],
            "fields": [
                {
                    "title": "Our Version",
                    "value": dep_info['version']
                },
                {
                    "title": "Patched Versions",
                    "value": v['patched_versions_string']
                },
                {
                    "title": "Unaffected Versions",
                    "value": unaffected
                }
            ],
            "ts": back_to_ts(dep_info['updated'])
        }
        attachments.append(attach)
    return attachments


def generateSecurityReport(response):
    vulnerable = []
    for dep in response['dependencies']:
        if dep['security_vulnerabilities']:
            dep_info = {
                'name': dep['name'],
                'version': dep['version_requested'],
                'updated': response['updated_at']
            }
            vulnerable.extend(formatVulnerabilities(dep['security_vulnerabilities'], dep_info))
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

def notify(params, response, notification_method='slack', notification_type='security'):
    formatted_report = notify_types[notification_types](response)
    send_report = notify_methods[notification_method](formatted_report, params)

sec_report = generateSecurityReport(test_report)
notifySlack({'slack_webhook': "WEBHOOK_HERE"}, sec_report)

def notifySlack(report):
    pass

def notifyEmail(report):
    pass

def notifyAll(report):
    notifySlack(formattedReport)
    notifyEmail(formattedReport)

def generateSecurityReport(response):
    pass

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

def notify(response, notification_method='slack', notification_type='all'):
    print("Beginning Notification")
    print(notification_method)
    print(notification_type)
    print(response.keys())

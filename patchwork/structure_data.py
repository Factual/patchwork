from .helpers import convert_versioneye_timestamp, current_time

top_level_fields = {
    'dep_number': 'total_dependencies',
    'out_number': 'total_outdated',
    'sv_count': 'total_vulnerabilities',
    'updated_at': 'scan_time'
}

dependency_fields = {
    'name': 'name',
    'version_current': 'version_available',
    'outdated': 'outdated',
}

vulnerability_fields = {
    'name_id': 'id',
    'summary': 'summary',
    'description': 'description',
    'publish_date': 'publish_date',
    'patched_versions_string': 'patched_versions',
    'unaffected_versions_string': 'unaffected_versions'
}

'''
report: raw output from VersionEye
file_path: path to dependency file that generated this report
'''
def structure_data(report, file_path):
    if type(report) is str:
        f = open(report, rb)
        report = json.loads(f)

    formatted = { top_level_fields[key]: report[key] for key in top_level_fields.keys() }
    time_string = formatted[top_level_fields['updated_at']]
    formatted[top_level_fields['updated_at']] = convert_versioneye_timestamp(time_string)
    dependencies = {}
    for d in report['dependencies']:
        dependency = { dependency_fields[key]: d[key] for key in dependency_fields.keys()}
        dependency['version_used'] = [
            { 'file': file_path, 'version': d['version_requested'] }
        ]
        vulnerabilities = None
        if d['security_vulnerabilities']:
            vulnerabilities = []
            for v in d['security_vulnerabilities']:
                vulnerability = { vulnerability_fields[key]: v[key] for key in vulnerability_fields.keys()}
                ts = vulnerability[vulnerability_fields['publish_date']]
                vulnerability[vulnerability_fields['publish_date']] = convert_versioneye_timestamp(ts)
                if 'links' in v and len(v['links']):
                    vulnerability['link'] = v['links'][list(v['links'])[0]]
                else:
                    vulnerability['link'] = None
                vulnerabilities.append(vulnerability)
        dependency['vulnerabilities'] = vulnerabilities
        dependencies[dependency['name']] = dependency
    formatted['dependencies'] = dependencies
    return formatted

def combine_dependencies(dependency1, dependency2):
    d = dict(dependency1)
    d['version_used'].extend(dependency2['version_used'])
    return d

def get_empty_report():
    return {
        'dependencies': {},
        'total_dependencies': 0,
        'total_vulnerabilities': 0,
        'total_outdated': 0,
        'scan_time': current_time()
    }

'''
Reports: formatted output of structure_data
'''
def combine_reports(report1, report2):
    dependencies = {}
    if 'dependencies' not in report1 and 'dependencies' not in report2:
        return get_empty_report()
    elif 'dependencies' not in report2:
        return report1
    elif 'dependencies' not in report1:
        return report2

    d1 = report1['dependencies']
    d2 = report2['dependencies']
    outdated_count = 0
    vulnerable_count = 0
    for dependency in d1:
        if dependency in d2:
            dependencies[dependency] = combine_dependencies(d1[dependency], d2[dependency])
        else:
            dependencies[dependency] = d1[dependency]
        if dependencies[dependency]['outdated']:
            outdated_count += 1
        if dependencies[dependency]['vulnerabilities'] != None:
            vulnerable_count += len(dependencies[dependency]['vulnerabilities'])
    for dependency in d2:
        if dependency not in dependencies:
            dependencies[dependency] = d2[dependency]
            if dependencies[dependency]['outdated']:
                outdated_count += 1
            if dependencies[dependency]['vulnerabilities'] != None:
                vulnerable_count += len(dependencies[dependency]['vulnerabilities'])
    return {
        'total_dependencies': len(dependencies),
        'total_outdated': outdated_count,
        'total_vulnerabilities': vulnerable_count,
        'scan_time': min(report1['scan_time'], report2['scan_time']),
        'dependencies': dependencies
    }

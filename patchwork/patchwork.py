#!/usr/local/bin/python3
import os, sys, getopt
import json
import requests
from .generate_notifications import notify
from .structure_data import *
from .helpers import *

VERBOSE = False
TEST = False
PERSIST = False
PATCHWORK_PATH = "/".join(os.path.realpath(__file__).split("/")[:-2])
PARAMETERS = {
    'directory': os.getcwd(),
    'directory_name': os.getcwd().split('/')[-1],
    'traversal_depth': 0,
    'subdirectory_blacklist': ['node_modules'],
    'dependency_file_types': ['package.json', 'Gemfile.lock', 'pom.xml', 'build.sbt', 'requirements.txt',
        'setup.py', 'biicode.conf', 'Berksfile.lock', 'project.json', 'packages.config',
        'Cargo.toml', 'Cargo.lock', 'yarn.lock', 'npm-shrinkwrap.json', 'bower.json', 'composer.json',
        'composer.lock', 'Podfile', 'Podfile.lock', 'project.clj', 'mix.exs'],
    'api_key': 'REPLACE_ME_IN_CONFIG_FILE',
    'api_organization': 'REPLACE_ME_IN_CONFIG_FILE',
    'data_directory': PATCHWORK_PATH + '/data/',
    'slack_webhook': 'REPLACE_ME_IN_CONFIG_FILE',
    'test_webhook': 'REPLACE_ME_IN_CONFIG_FILE'
}

class VersionEyeException(Exception):
    pass

"""
:param config_file: str Path to json file with unique config parameters (api_key, project_key at minimum)
:returns: dict Concatenation of default parameters with overrides from the config_file
"""
def parse_parameters(config_file = ''):
    if not config_file: return
    global PARAMETERS
    with open(config_file) as json_file:
        parameters = json.load(json_file)
        parameters = {k: v for k, v in parameters.items() if v != 'DEFAULT'}
        PARAMETERS = {**PARAMETERS, **parameters}

"""
Traverse directory up to depth traversal_depth looking for dependency_file_types

:returns: dict All paths to specified dependency_file_types, keyed by each dependency_file_type
"""
def find_dependency_files():
    dependency_file_paths = {}
    for f in PARAMETERS['dependency_file_types']:
        dependency_file_paths[f] = []

    rootDir = PARAMETERS["directory"]
    baselevel = len(rootDir.split("/"))
    for dirName, subdirList, fileList in os.walk(rootDir):
        for subdir in PARAMETERS['subdirectory_blacklist']:
            if subdir in subdirList: subdirList.remove(subdir)
        level = len(dirName.split("/")) - baselevel
        if level >= (PARAMETERS['traversal_depth']): del subdirList[:]
        for f in fileList:
            if f in PARAMETERS['dependency_file_types']:
                if VERBOSE: print(get_display_name(dirName, PARAMETERS), 'has a', f)
                full_path_to_dependency = "{0}/{1}".format(dirName, f)
                dependency_file_paths[f].append(full_path_to_dependency)
    return dependency_file_paths

"""
Fetches VersionEye report for a given file

:params dependency_file_path: str Path of dependency file to upload to VersionEye

:params save_dir: str Path to directory where returned report should be saved
:returns: Dict JSON report from VersionEye
"""
def look_up_file(dependency_file_path):
    POST_PROJECT = 'https://www.versioneye.com/api/v2/projects/{1}?api_key={0}'.format(PARAMETERS['api_key'], PARAMETERS['project_key'])

    files = {'project_file': open(dependency_file_path,'rb')}
    data = {'project_key': PARAMETERS['project_key']}
    advisory = requests.post(POST_PROJECT, files=files, data=data)
    if advisory.status_code != 201:
        print('Error:', advisory.status_code)
        print(advisory.json())
        delete_project()
        raise VersionEyeException
    return advisory.json()

"""
Finds or creates new folder for VersionEye reports.
If name is not provided, creates a new folder based on the timestamp.

:params name: str Optional - desired name of subdirectory
:returns: str Path to subdirectory
"""
def get_directory_for_reports(name = ''):
    if not PERSIST:
        return ''
    if not name:
        name = get_datetime()
    top_directory = PARAMETERS['data_directory']
    data_path = top_directory + name
    if not os.path.exists(top_directory):
        os.makedirs(top_directory)
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    return data_path

"""
:returns: true iff the VersionEye report contains depdendencies that are either outdated or vulnerable.
"""
def problems_detected(report):
    return report['total_outdated'] or report['total_vulnerabilities']

'''
:param files: dict Keyed by file type, list of dependency files. Output of find_dependency_files
:param directory: string Optional - directory to save combined file type report to
:returns: dict with { file_type: combined_report } entries
'''
def combined_reports_by_file_type(files, directory):
    type_reports = {}
    for ftype in files:
        combined_report = {}
        for fname in files[ftype]:
            if VERBOSE: print("Uploading {0}...".format(get_display_name(fname, PARAMETERS)))
            raw_report = look_up_file(fname)
            report_fname = get_display_name(fname, PARAMETERS)
            formatted_report = structure_data(raw_report, report_fname)
            if combined_report:
                combined_report = combine_reports(combined_report, formatted_report)
            else:
                combined_report = formatted_report
        type_reports[ftype] = combined_report
        if PERSIST:
            report_path = directory + '/' + ftype + '_data.json'
            with open(report_path, 'w') as outfile:
                json.dump(combined_report, outfile, indent=4, separators=(',', ': '))
    if VERBOSE: print("Upload Completed")
    return type_reports


'''
Gets full, formatted report given either file_type combined reports or dependency files dict
Must provide either files or file_type_reports

:param files: dict Keyed by file type, list of dependency files. Output of find_dependency_files
:param file_type_reports: dict Keyed by file type, combined json reports.
        Output of combined_reports_by_file_type
:param directory: string Optional - directory to save combined report to
:returns: (path_of_saved_report, combined_report_as_dict)
'''
def combined_reports_all(files = {}, file_type_reports = {}, directory = ''):
    save_directory = get_directory_for_reports(directory)
    if not file_type_reports:
        if VERBOSE: print("Fetching combined reports by file type...")
        file_type_reports = combined_reports_by_file_type(files, save_directory)

    all_reports = []
    path_name = save_directory + '/combined.json'
    for ftype in file_type_reports:
        all_reports.append(file_type_reports[ftype])

    combined_report = all_reports[0]
    if len(all_reports) > 1:
        for report in all_reports[1:]:
            combined_report = combine_reports(combined_report, report)

    if PERSIST:
        with open(path_name, 'w') as report_file:
            json.dump(combined_report, report_file, indent=4, separators=(',', ': '))
    return (path_name, combined_report)

def create_project():
    empty_upload_file = PATCHWORK_PATH + '/patchwork/package.json'
    create_path = 'https://www.versioneye.com/api/v2/projects?api_key={0}'.format(PARAMETERS['api_key'])
    files = {'upload': open(empty_upload_file,'rb')}
    data = {'orga_name': PARAMETERS['api_organization'], 'temp': True}
    project = requests.post(create_path, files=files, data=data)
    if project.status_code != 201:
        print('Error:', project.status_code)
        print(project.json())
        raise VersionEyeException
    return project.json()['id']

def delete_project(key=''):
    if not key:
        key = PARAMETERS['project_key']
    delete_path = 'https://www.versioneye.com/api/v2/projects/{1}?api_key={0}'.format(PARAMETERS['api_key'], key)
    req = requests.delete(delete_path)
    if req.status_code != 200:
        print('Error:', req.status_code)
        print(req.json())
        raise VersionEyeException

'''
Sets global variables based on command line options
Returns path to config file
'''
def parse_args(argv):
    helpstring = 'dep-check.py [-c <config_file>] [-v -t -s]'

    fname = PATCHWORK_PATH + '/patchwork/config.json' # if not specified, look in current directory
    global VERBOSE
    global TEST
    global PERSIST
    try:
        opts, args = getopt.getopt(argv,"hvtsc:",["verbose","test","save","config="])
    except getopt.GetoptError:
        print(helpstring)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(helpstring)
            sys.exit()
        elif opt in ("-c", "--config"):
            fname = arg
        elif opt in ("-v", "--verbose"):
            VERBOSE = True
        elif opt in ("-t", "--test"):
            TEST = True
        elif opt in ("-s", "--save"):
            PERSIST = True
    return fname

def main():
    config_file_path = parse_args(sys.argv[1:])
    parse_parameters(config_file_path)
    files = find_dependency_files()
    PARAMETERS['project_key'] = create_project()
    report_path, report = combined_reports_all(files=files)
    delete_project()
    if problems_detected(report):
        if TEST:
            slack_params = { "webhook": PARAMETERS["test_webhook"] }
        else:
            slack_params = { "webhook": PARAMETERS["slack_webhook"] }
        notify(slack_params, report)

if __name__ == "__main__":
    main()

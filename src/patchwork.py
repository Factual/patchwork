#!/usr/local/bin/python3
import os, sys, getopt
import json
import requests
from generate_notifications import notify
from structure_data import *
from helpers import *

VERBOSE = False
DEFAULT_PARAMETERS = {
    'directory': '/',
    'report_directory': '/',
    'traversal_depth': 1,
    'subdirectory_blacklist': ['node_modules'],
    'dependency_file_types': ['package.json'],
    'api_key': 'REPLACE_ME_IN_CONFIG_FILE',
    'project_key': 'REPLACE_ME_IN_CONFIG_FILE',
    'report_directory': 'data/'
}

class VersionEyeException(Exception):
    pass

"""
:param config_file: str Path to json file with unique config parameters (api_key, project_key at minimum)
:returns: dict Concatenation of default parameters with overrides from the config_file
"""
def parse_parameters(config_file = ''):
    if not config_file: return DEFAULT_PARAMETERS
    parameters = {}
    with open(config_file) as json_file:
        parameters = json.load(json_file)
    return {**DEFAULT_PARAMETERS, **parameters}

"""
Traverse directory up to depth traversal_depth looking for dependency_file_types

:param parameters: dict Result of parse_parameters, with entries for tree traversal -
                        directory: str Path of top level directory to search
                        traversal_depth: int Max depth of nested subtrees to search
                        dependency_file_types: [str] File names to match against
:returns: dict All paths to specified dependency_file_types, keyed by each dependency_file_type
"""
def find_dependency_files(parameters):
    dependency_file_paths = {}
    for f in parameters['dependency_file_types']:
        dependency_file_paths[f] = []

    rootDir = parameters["directory"]
    baselevel = len(rootDir.split("/"))
    for dirName, subdirList, fileList in os.walk(rootDir):
        for subdir in parameters['subdirectory_blacklist']:
            if subdir in subdirList: subdirList.remove(subdir)
        level = len(dirName.split("/")) - baselevel
        if level >= (parameters['traversal_depth']): del subdirList[:]
        for f in fileList:
            if f in parameters['dependency_file_types']:
                if VERBOSE: print(get_display_name(dirName, params), 'has a', f)
                full_path_to_dependency = "{0}/{1}".format(dirName, f)
                dependency_file_paths[f].append(full_path_to_dependency)
    return dependency_file_paths

"""
Fetches VersionEye report for a given file

:params dependency_file_path: str Path of dependency file to upload to VersionEye
:params parameters: dict Result of parse_parameters, with entries for VersionEye access -
                        api_key: str VersionEye api key
                        project_key: str ID of VersionEye project to update
                        directory: str Path of top level directory being searched
:params save_dir: str Path to directory where returned report should be saved
:returns: Dict JSON report from VersionEye
"""
def look_up_file(dependency_file_path, parameters, save_dir=''):
    POST_PROJECT = 'https://www.versioneye.com/api/v2/projects/{1}?api_key={0}'.format(parameters['api_key'], parameters['project_key'])
    file_name = dependency_file_path.split(parameters['directory'])[1][1:] + "_data.json"
    file_path = save_dir + '/' + file_name.replace('/','_')

    files = {'project_file': open(dependency_file_path,'rb')}
    data = {'project_key': parameters['project_key']}
    advisory = requests.post(POST_PROJECT, files=files, data=data)
    if advisory.status_code != 201:
        print('Error:', advisory.status_code)
        print(advisory.json())
        raise VersionEyeException
    if save_dir:
        with open(file_path, 'w') as outfile:
            json.dump(advisory.json(), outfile)
    return advisory.json()

"""
Finds or creates new folder for VersionEye reports.
If name is not provided, creates a new folder based on the timestamp.

:params top_directory: str Directory under which to create new subdirectory
:params name: str Optional - desired name of subdirectory
:returns: str Path to subdirectory
"""
def get_directory_for_reports(top_directory, name = ''):
    if not name:
        name = get_datetime()
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
:param individual_directory: string Option - directory to save individual file reports to
:returns: dict with { file_type: combined_report } entries
'''
def combined_reports_by_file_type(files, directory = '', individual_directory = ''):
    type_reports = {}
    for ftype in files:
        combined_report = {}
        for fname in files[ftype]:
            if VERBOSE: print("Uploading {0}...".format(get_display_name(fname, params)))
            raw_report = look_up_file(fname, params, individual_directory)
            report_fname = get_display_name(fname, params)
            formatted_report = structure_data(raw_report, report_fname)
            if combined_report:
                combined_report = combine_reports(combined_report, formatted_report)
            else:
                combined_report = formatted_report
        type_reports[ftype] = combined_report
        if directory:
            report_path = dirname + '/' + ftype + '.json'
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
def combined_reports_all(files = {}, file_type_reports = {}, directory = '', persist=False):
    if not directory and persist:
        directory = get_directory_for_reports('data/')
    if not file_type_reports:
        if VERBOSE: print("Fetching combined reports by file type...")
        file_type_reports = combined_reports_by_file_type(files)

    all_reports = []
    combined_report = {}

    path_name = directory + '/combined.json'
    for ftype in file_type_reports:
        all_reports.append(file_type_reports[ftype])
    combined_report = all_reports[0]
    for report in all_reports[1:]:
        combined_report = combine_reports(combined_report, report)
    if persist:
        with open(path_name, 'w') as report_file:
            json.dump(combined_report, report_file, indent=4, separators=(',', ': '))
    return (path_name, combined_report)

def parse_args(argv):
    helpstring = 'dep-check.py -c <config_file> [-v]'
    fname = os.getcwd() + '/config.json' # if not specified, look in current directory
    global VERBOSE
    try:
        opts, args = getopt.getopt(argv,"hvc:",["verbose","config="])
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
    return fname

if __name__ == "__main__":
    config_file_path = parse_args(sys.argv[1:])
    params = parse_parameters(config_file_path)
    files = find_dependency_files(params)
    report_path, report = combined_reports_all(files=files)
    if problems_detected(report):
        notify(params, report)

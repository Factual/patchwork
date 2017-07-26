#!/usr/local/bin/python3
import os, sys, getopt
import json
import requests
import time, datetime
from generate_notifications import notify

VERBOSE = False
DEFAULT_PARAMETERS = {
    'directory': '/',
    'traversal_depth': 1,
    'subdirectory_blacklist': ['node_modules'],
    'dependency_file_types': ['package.json'],
    'api_key': 'REPLACE_ME_IN_CONFIG_FILE',
    'project_key': 'REPLACE_ME_IN_CONFIG_FILE',
    'report_directory': 'data/'
}

def parse_parameters(config_file):
    if not config_file: return DEFAULT_PARAMETERS
    parameters = {}
    with open(config_file) as json_file:
        parameters = json.load(json_file)
    return {**DEFAULT_PARAMETERS, **parameters}

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
                if VERBOSE: print(dirName, 'has a', f)
                full_path_to_dependency = "{0}/{1}".format(dirName, f)
                dependency_file_paths[f].append(full_path_to_dependency)
    return dependency_file_paths

def look_up_file(dependency_file_path, parameters, save_dir=''):
    POST_PROJECT = 'https://www.versioneye.com/api/v2/projects/{1}?api_key={0}'.format(parameters['api_key'], parameters['project_key'])
    file_name = dependency_file_path.split(parameters['directory'])[1][1:] + "_data.json"
    file_path = save_dir + '/' + file_name.replace('/','_')
    print(file_path)

    files = {'project_file': open(dependency_file_path,'rb')}
    values = {
        'project_key': parameters['project_key']
    }

    advisory = requests.post(POST_PROJECT, files=files, data=values)
    if save_dir:
        print("saving")
        with open(file_path, 'w') as outfile:
            json.dump(advisory.json(), outfile)
    return advisory.json()

def get_directory_for_reports(top_directory, name = ''):
    if not name:
        name = datetime.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d--%H_%M')
    data_path = top_directory + name
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    return data_path

def problems_detected(data):
    return data['out_number'] or data['sv_count']

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
    report = look_up_file(files['package.json'][0], params, get_directory_for_reports(params['report_directory']))
    if problems_detected(report):
        notify(report, 'slack', 'all')

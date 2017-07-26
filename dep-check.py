#!/usr/local/bin/python3
import os, sys, getopt
import json

CONFIG_FILE_PATH = '/Users/laura/dependency_monitoring/config.json'
VERBOSE = True
DEFAULT_PARAMETERS = {
    'traversal_depth': 1,
    'subdirectory_blacklist': ['node_modules'],
    "dependency_file_types": ["package.json"]
}

def parse_parameters(config_file):
    parameters = {}
    with open(config_file) as json_file:
        parameters = json.load(json_file)
    return {**DEFAULT_PARAMETERS, **parameters}

def find_dependency_files(parameters):
    print(parameters)
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

find_dependency_files(parse_parameters(CONFIG_FILE_PATH))

def parse_args(argv):
    directory = ''
    filename = ''
    helpstring = 'dep-check.py -d <directory> | -f <file>'
    try:
        opts, args = getopt.getopt(argv,"hd:f:",["directory=","file="])
    except getopt.GetoptError:
        print(helpstring)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(helpstring)
            sys.exit()
        elif opt in ("-d", "--directory"):
            directory = arg
        elif opt in ("-f", "--file"):
            filename = arg

if __name__ == "__main__":
    parse_args(sys.argv[1:])

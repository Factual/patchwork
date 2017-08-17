#!/usr/local/bin/python3
import json
import sys, os

def config_vim():

    EDITOR = os.environ.get('EDITOR', 'vim')
    path_to_file = "/".join(os.path.realpath(__file__).split("/")[:-1]) + '/config.json'

    print('This command will open your preferred editor (default vim) to configure Patchwork.')
    print('\tYou must provide your VersionEye and Slack information to use Patchwork.')
    print('\tOther options can be configured by overriding the "DEFAULT" tag.')
    input('Press Enter to Continue: ')

    os.system(EDITOR + " " + path_to_file)

    print()
    print('Your configurations have been saved.')

def main():
    config_vim()
    print('You can now use the "patchwork" command to run patchwork')

if __name__ == '__main__':
    main()

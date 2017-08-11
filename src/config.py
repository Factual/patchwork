#!/usr/local/bin/python3
import json

def config():
    api_key = input("Please enter your VersionEye API Key: ")
    api_name = input("Please enter your VersionEye organization name (like '<username>_orga'): ")
    webhook = input("Please enter the webhook for your Slack integration: ")
    # TODO validate inputs
    config_json = {
        'api_key': api_key,
        'api_organization': api_name,
        'slack_webhook': webhook,
    }
    with open('config.json', 'w') as outfile:
        json.dump(config_json, outfile, indent=4, separators=(',', ': '))

if __name__ == '__main__':
    config()
    print('You can now use the "patchwork" command to run patchwork')

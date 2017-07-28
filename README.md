# Patchwork -- Dependency Monitoring for the Front Team

## Factual Hackathon 2017

Project to help Front (& potentially other teams) manage versioning upates and security vulnerabilities in 3rd party package dependencies.

## Types of Notifications
### Versioning

![Versioning Notification](https://user-images.githubusercontent.com/10542153/28694551-2936dc10-72df-11e7-9f27-8e223754fd03.png)

Distinguishes between minor releases, middling releases, and new major version numbers.

### Security

![Security Notification](https://user-images.githubusercontent.com/10542153/28694576-58d56a86-72df-11e7-86ea-bf0a1eb7d925.png)

Orange for security vulnerabilities published more than 2 weeks ago, red if published within the last two weeks (most recent sprint).

## Setup Patchwork

### Create VersionEye Account

[Signup](https://www.versioneye.com/signup?utf8=%E2%9C%93) for an account at https://www.versioneye.com/signup?utf8=%E2%9C%93. Make note of your API Key.

#### Initialize VersionEye Project

Initialize your VersionEye project by uploading one of your dependency files from the sidebar of your VersionEye page (Projects >> --Create From Upload). If you click on the project (named after the file you uploaded), you can see the project key in parentheses next to "Name:" at the top of the page. Make note of this key. You can also change the project name if you wish by hitting the pencil button at the end of the line.

### Create a SlackBot

Create a new app at https://api.slack.com/apps. Title it 'Patchwork'.

In 'Add Features and Functionality', click 'Incoming Webhooks'. At the bottom, click 'Add New Webhook to Team' and follow the instructions to choose the channel the app will post to. Make note of the generated webhook URL.

Upload the Patchwork logo from `patchwork/assets/patchwork.png` under "Basic Information > Display Information". I chose "Notices for Package Updates & Security Vulnerabilities" for the description and `#c55100` for the background color.

### Create your config file

In `patchwork/src`, copy `config.json.example` to `config.json` and edit the resulting file as necessary.
The API key, project key, and Slack webhook URL you just generated are required.
Delete any lines of this file that you do not want - they will override the default values if they are set.

## Run Patchwork

`cd` into `patchwork/src` and run `chmod +x dep-check.py` to make the dependency checker executable.
Run via `./dep-check.py`, or `./dep-check.py -v` for verbose mode.

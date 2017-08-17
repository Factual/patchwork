# Patchwork -- Dependency Monitoring

## Factual Hackathon 2017

Project to help Factual's Front Team manage versioning upates and security vulnerabilities in 3rd party package dependencies.
Offered as-is with no plans for further updates.

## Setup Patchwork

### Create VersionEye Account

[Signup](https://www.versioneye.com/signup?utf8=%E2%9C%93) for an account at https://www.versioneye.com/signup?utf8=%E2%9C%93. Make note of your API Key and organization name.
The organization name is found at the top of your VersionEye dashboard when logged in and will be something like `[username]_orga`.

### Create a SlackBot

Create a new app at https://api.slack.com/apps. Title it 'Patchwork'.

In 'Add Features and Functionality', click 'Incoming Webhooks'. At the bottom, click 'Add New Webhook to Team' and follow the instructions to choose the channel the app will post to. Make note of the generated webhook URL.

Upload the Patchwork logo from `patchwork/assets/patchwork.png` under "Basic Information > Display Information". I chose "Notices for Package Updates & Security Vulnerabilities" for the description and `#c55100` for the background color.

### Create your config file

In `patchwork/patchwork`, fill out `config.json` as necessary. If you downloaded the `factual-patchwork` package via `pip3`, you can also just run `patchwork-config`.
The API key, organization name, and Slack webhook URL you just generated are required.
To keep the defaults for a parameter, use the `"DEFAULT"` key or delete the line entirely.

#### Other Config Options

##### `directory`

str: Absolute path of the directory to search for outdated dependencies. Default is the directory which `patchwork` is called from.

##### `directory_name`

str: Name of the directory to search for outdated dependencies. Used in place of the absolute path in reporting: for example, if a dependency is at `/Users/yourName/repo_name/dependency.type` and directory_name is set to `repo_name`, Slack and email notifications will refer to the file by `repo_name/dependency.type` instead of the full path on your machine.

##### `traversal_depth`

int: represents how deeply to search for dependency files. For example, the default `traversal_depth = 0` represents only searching in the top-level directory and will return files like `repository/package.json` but not `repository/src/package.json`.

##### `subdirectory_blacklist`

str[]: Patchwork will ignore any subdirectories with the included names. By default, Patchwork blacklists `node_modules` subdirectories so you don't waste API calls looking up your dependencies' dependencies. For an even more thorough search that includes all these files, you can override this setting in your config file with `subdirectory_blacklist: []`.

##### `test_webhook`

str: If using the `-t` or `--test` option, sends Slack notifications to this webhook. This option allows you to post to a different channel (I recommend your own slackbot channel) when testing so you don't overwhelm the real channel.

##### `dependency_file_types`

str[]: Patchwork searches for and uploads to VersionEye only those files that match a file name in this array. Default is `['package.json']`. See below for more options:

###### <a name="dependency-types"></a>Supported Dependency Options

- pom.xml
- build.sbt
- Gemfile.lock
- requirements.txt
- setup.py
- biicode.conf
- Berksfile.lock
- project.json
- packages.config
- Cargo.toml
- Cargo.lock
- package.json
- yarn.lock
- npm-shrinkwrap.json
- bower.json
- composer.json
- composer.lock
- Podfile
- Podfile.lock
- project.clj
- mix.exs

### Install Requirements

Patchwork requires python3.
Install python3 from https://www.python.org/downloads/.
Patchwork does not require any nonstandard libraries.

If your copy of python3 is anywhere other than `usr/local/bin/python3`, you may have to update the shebang on line 1 of `patchwork/src/patchwork.py` with the path to your copy. The path can be found with `which python3`.

You can also install Patchwork via `pip3 install factual-patchwork`. This is the recommended way to install Patchwork if you do not wish to do any customization in the code.

## Run Patchwork

Recommended: 
```
pip3 install factual-patchwork
patchwork-config
patchwork
```

`cd` into `patchwork/src` and run `chmod +x patchwork.py` to make the dependency checker executable.
Run via `./patchwork.py`, or `./patchwork.py -v` for verbose mode.

Use the `-t` option to run in test mode (posts to a different Slack channel).

## Types of Notifications
### Versioning

![Versioning Notification](https://user-images.githubusercontent.com/10542153/28694551-2936dc10-72df-11e7-9f27-8e223754fd03.png)

Distinguishes between minor releases, middling releases, and new major version numbers.

### Security

![Security Notification](https://user-images.githubusercontent.com/10542153/28694576-58d56a86-72df-11e7-86ea-bf0a1eb7d925.png)

Orange for security vulnerabilities published more than 2 weeks ago, red if published within the last two weeks (most recent sprint).

## License

MIT License

Copyright (c) 2017 Factual, Inc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

report = {
  "id": "597905b5368b08001690833e",
  "name": "front",
  "project_type": "npm",
  "organisation": {
    "name": "leckman_orga",
    "company": None,
    "location": None
  },
  "public": True,
  "private_scm": True,
  "source": "API",
  "dep_number": 195,
  "out_number": 122,
  "licenses_red": 22,
  "licenses_unknown": 12,
  "sv_count": 10,
  "dep_number_sum": 195,
  "out_number_sum": 122,
  "unknown_number_sum": 0,
  "licenses_red_sum": 22,
  "licenses_unknown_sum": 12,
  "sv_count_sum": 10,
  "created_at": "2017-07-26T21:12:22.673Z",
  "updated_at": "2017-07-27T00:59:31.072Z",
  "license_whitelist": "default_lwl",
  "dependencies": [
    {
      "name": "mail_form",
      "prod_key": "mail_form",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "1.7.0",
      "version_requested": "1.5.0",
      "comparator": "=",
      "unknown": False,
      "outdated": True,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://opensource.org/licenses/mit-license.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "actionmailer",
      "prod_key": "actionmailer",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "5.1.2",
      "version_requested": "5.0.0",
      "comparator": "=",
      "unknown": False,
      "outdated": True,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://spdx.org/licenses/MIT.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "nio4r",
      "prod_key": "nio4r",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "2.1.0",
      "version_requested": "1.2.1",
      "comparator": "=",
      "unknown": False,
      "outdated": True,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://spdx.org/licenses/MIT.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "activejob",
      "prod_key": "activejob",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "5.1.2",
      "version_requested": "5.0.0",
      "comparator": "=",
      "unknown": False,
      "outdated": True,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://spdx.org/licenses/MIT.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "mail",
      "prod_key": "mail",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "2.6.6",
      "version_requested": "2.6.4",
      "comparator": "=",
      "unknown": False,
      "outdated": True,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://spdx.org/licenses/MIT.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "globalid",
      "prod_key": "globalid",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "0.4.0",
      "version_requested": "0.3.7",
      "comparator": "=",
      "unknown": False,
      "outdated": True,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://spdx.org/licenses/MIT.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "nokogiri",
      "prod_key": "nokogiri",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "1.8.0",
      "version_requested": "1.6.8",
      "comparator": "=",
      "unknown": False,
      "outdated": True,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://spdx.org/licenses/MIT.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": [
        {
          "language": "Ruby",
          "prod_key": "nokogiri",
          "name_id": "CVE-2016-4658",
          "author": None,
          "summary": "Nokogiri gem contains several vulnerabilities in libxml2 and libxslt",
          "description": "Nokogiri version 1.7.1 has been released, pulling in several upstream\npatches to the vendored libxml2 to address the following CVEs:\n\nCVE-2016-4658\nCVSS v3 Base Score: 9.8 (Critical)\nlibxml2 in Apple iOS before 10, OS X before 10.12, tvOS before 10, and\nwatchOS before 3 allows remote attackers to execute arbitrary code or cause\na denial of service (memory corruption) via a crafted XML document.\n\nCVE-2016-5131\nCVSS v3 Base Score: 8.8 (HIGH)\nUse-after-free vulnerability in libxml2 through 2.9.4, as used in Google\nChrome before 52.0.2743.82, allows remote attackers to cause a denial of\nservice or possibly have unspecified other impact via vectors related to\nthe XPointer range-to function.\n",
          "platform": None,
          "osvdb": None,
          "cve": "2016-4658",
          "cvss_v2": None,
          "publish_date": "2017-03-11",
          "framework": None,
          "affected_versions_string": None,
          "affected_versions": [
            "1.5.2",
            "1.5.1",
            "1.5.1.rc1",
            "1.5.0",
            "1.4.7",
            "1.4.6",
            "1.4.5",
            "1.5.0.beta.4",
            "1.5.0.beta.3",
            "1.4.4.2",
            "1.4.4.1",
            "1.4.4",
            "1.5.0.beta.2",
            "1.4.3.1",
            "1.4.3",
            "1.5.0.beta.1",
            "1.4.2.1",
            "1.4.2",
            "1.4.1",
            "1.4.0",
            "1.3.3",
            "1.3.2",
            "1.3.1",
            "1.3.0",
            "1.2.3",
            "1.2.2",
            "1.2.1",
            "1.2.0",
            "1.1.1",
            "1.1.0",
            "1.0.7",
            "1.0.6",
            "1.0.5",
            "1.0.4",
            "1.0.3",
            "1.0.2",
            "1.0.1",
            "1.0.0",
            "1.5.3.rc2",
            "1.5.3.rc3",
            "1.5.3.rc4",
            "1.5.3.rc5",
            "1.5.4.rc1",
            "1.5.3",
            "1.5.3.rc6",
            "1.5.4.rc3",
            "1.5.4.rc2",
            "1.5.4",
            "1.5.5.rc1",
            "1.5.5.rc2",
            "1.5.5.rc3",
            "1.5.5",
            "1.5.6.rc1",
            "1.5.6.rc2",
            "1.5.6.rc3",
            "1.5.6",
            "1.5.7.rc1",
            "1.5.7.rc2",
            "1.5.7.rc3",
            "1.5.8",
            "1.5.7",
            "1.5.9",
            "1.6.0.rc1",
            "1.5.10",
            "1.6.0",
            "1.6.1",
            "1.5.11",
            "1.6.2.rc1",
            "1.6.2.rc2",
            "1.6.2.rc3",
            "1.6.2",
            "1.6.2.1",
            "1.6.3.rc1",
            "1.6.3.rc2",
            "1.6.3.rc3",
            "1.6.3.1",
            "1.6.3",
            "1.6.4",
            "1.6.4.1",
            "1.6.5",
            "1.6.6.1",
            "1.6.6.2",
            "1.6.7.rc2",
            "1.6.7.rc3",
            "1.6.6.3",
            "1.6.6.4",
            "1.6.7.rc4",
            "1.6.7",
            "1.6.8.rc1",
            "1.6.7.1",
            "1.6.8.rc2",
            "1.6.7.2",
            "1.6.8.rc3",
            "1.6.8",
            "1.6.8.1",
            "1.7.0",
            "1.7.0.1"
          ],
          "patched_versions_string": ">= 1.7.1",
          "unaffected_versions_string": "",
          "links": {
            "URL": "https://github.com/sparklemotion/nokogiri/issues/1615"
          }
        },
        {
          "language": "Ruby",
          "prod_key": "nokogiri",
          "name_id": "CVE-2017-5029",
          "author": None,
          "summary": "Nokogiri gem contains two upstream vulnerabilities in libxslt 1.1.29",
          "description": "nokogiri version 1.7.2 has been released.\n\nThis is a security update based on 1.7.1, addressing two upstream\nlibxslt 1.1.29 vulnerabilities classified as \"Medium\" by Canonical \nand given a CVSS3 score of \"6.5 Medium\" and \"8.8 High\" by RedHat.\n\nThese patches only apply when using Nokogiri's vendored libxslt\npackage. If you're using your distro's system libraries, there's no\nneed to upgrade from 1.7.0.1 or 1.7.1 at this time.\n\nFull details are available at the github issue linked to in the\nchangelog below.\n\n-----\n\n# 1.7.2 / 2017-05-09\n\n## Security Notes\n\n[MRI] Upstream libxslt patches are applied to the vendored libxslt\n1.1.29 which address CVE-2017-5029 and CVE-2016-4738.\n\nFor more information:\n\n* https://github.com/sparklemotion/nokogiri/issues/1634\n* http://people.canonical.com/~ubuntu-security/cve/2017/CVE-2017-5029.html\n* http://people.canonical.com/~ubuntu-security/cve/2016/CVE-2016-4738.html\n",
          "platform": None,
          "osvdb": None,
          "cve": "2017-5029",
          "cvss_v2": None,
          "publish_date": "2017-05-09",
          "framework": None,
          "affected_versions_string": None,
          "affected_versions": [
            "1.5.2",
            "1.5.1",
            "1.5.1.rc1",
            "1.5.0",
            "1.4.7",
            "1.4.6",
            "1.4.5",
            "1.5.0.beta.4",
            "1.5.0.beta.3",
            "1.4.4.2",
            "1.4.4.1",
            "1.4.4",
            "1.5.0.beta.2",
            "1.4.3.1",
            "1.4.3",
            "1.5.0.beta.1",
            "1.4.2.1",
            "1.4.2",
            "1.4.1",
            "1.4.0",
            "1.3.3",
            "1.3.2",
            "1.3.1",
            "1.3.0",
            "1.2.3",
            "1.2.2",
            "1.2.1",
            "1.2.0",
            "1.1.1",
            "1.1.0",
            "1.0.7",
            "1.0.6",
            "1.0.5",
            "1.0.4",
            "1.0.3",
            "1.0.2",
            "1.0.1",
            "1.0.0",
            "1.5.3.rc2",
            "1.5.3.rc3",
            "1.5.3.rc4",
            "1.5.3.rc5",
            "1.5.4.rc1",
            "1.5.3",
            "1.5.3.rc6",
            "1.5.4.rc3",
            "1.5.4.rc2",
            "1.5.4",
            "1.5.5.rc1",
            "1.5.5.rc2",
            "1.5.5.rc3",
            "1.5.5",
            "1.5.6.rc1",
            "1.5.6.rc2",
            "1.5.6.rc3",
            "1.5.6",
            "1.5.7.rc1",
            "1.5.7.rc2",
            "1.5.7.rc3",
            "1.5.8",
            "1.5.7",
            "1.5.9",
            "1.6.0.rc1",
            "1.5.10",
            "1.6.0",
            "1.6.1",
            "1.5.11",
            "1.6.2.rc1",
            "1.6.2.rc2",
            "1.6.2.rc3",
            "1.6.2",
            "1.6.2.1",
            "1.6.3.rc1",
            "1.6.3.rc2",
            "1.6.3.rc3",
            "1.6.3.1",
            "1.6.3",
            "1.6.4",
            "1.6.4.1",
            "1.6.5",
            "1.6.6.1",
            "1.6.6.2",
            "1.6.7.rc2",
            "1.6.7.rc3",
            "1.6.6.3",
            "1.6.6.4",
            "1.6.7.rc4",
            "1.6.7",
            "1.6.8.rc1",
            "1.6.7.1",
            "1.6.8.rc2",
            "1.6.7.2",
            "1.6.8.rc3",
            "1.6.8",
            "1.6.8.1",
            "1.7.0",
            "1.7.0.1",
            "1.7.1"
          ],
          "patched_versions_string": ">= 1.7.2",
          "unaffected_versions_string": "",
          "links": {
            "URL": "https://github.com/sparklemotion/nokogiri/issues/1634"
          }
        }
      ]
    },
    {
      "name": "bcrypt",
      "prod_key": "bcrypt",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "3.1.11",
      "version_requested": "3.1.11",
      "comparator": "=",
      "unknown": False,
      "outdated": False,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://spdx.org/licenses/MIT.html",
          "on_whitelist": True,
          "on_cwl": None
        },
        {
          "name": "Apache-2.0",
          "url": "https://raw.githubusercontent.com/dstufft/bcrypt/master/LICENSE",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "better_errors",
      "prod_key": "better_errors",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "2.1.1",
      "version_requested": "2.1.1",
      "comparator": "=",
      "unknown": False,
      "outdated": False,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://spdx.org/licenses/MIT.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "coderay",
      "prod_key": "coderay",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "1.1.1",
      "version_requested": "1.1.1",
      "comparator": "=",
      "unknown": False,
      "outdated": False,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://spdx.org/licenses/MIT.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "binding_of_caller",
      "prod_key": "binding_of_caller",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "0.7.2",
      "version_requested": "0.7.2",
      "comparator": "=",
      "unknown": False,
      "outdated": False,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "https://github.com/banister/binding_of_caller/blob/master/LICENSE",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "debug_inspector",
      "prod_key": "debug_inspector",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "0.0.3",
      "version_requested": "0.0.2",
      "comparator": "=",
      "unknown": False,
      "outdated": True,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "https://raw.githubusercontent.com/banister/debug_inspector/master/README.md",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "bootstrap-sass",
      "prod_key": "bootstrap-sass",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "3.3.7",
      "version_requested": "3.3.7",
      "comparator": "=",
      "unknown": False,
      "outdated": False,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://spdx.org/licenses/MIT.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "sass",
      "prod_key": "sass",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "3.5.1",
      "version_requested": "3.4.22",
      "comparator": "=",
      "unknown": False,
      "outdated": True,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://spdx.org/licenses/MIT.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "byebug",
      "prod_key": "byebug",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "9.0.6",
      "version_requested": "9.0.5",
      "comparator": "=",
      "unknown": False,
      "outdated": True,
      "stable": True,
      "licenses": [
        {
          "name": "BSD",
          "url": "http://spdx.org/licenses/BSD.html",
          "on_whitelist": True,
          "on_cwl": None
        },
        {
          "name": "BSD-2-Clause",
          "url": "https://raw.githubusercontent.com/deivid-rodriguez/byebug/master/LICENSE",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "capybara",
      "prod_key": "capybara",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "2.14.4",
      "version_requested": "2.7.1",
      "comparator": "=",
      "unknown": False,
      "outdated": True,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://spdx.org/licenses/MIT.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "mime-types",
      "prod_key": "mime-types",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "3.1",
      "version_requested": "2.99.2",
      "comparator": "=",
      "unknown": False,
      "outdated": True,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://spdx.org/licenses/MIT.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "xpath",
      "prod_key": "xpath",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "2.1.0",
      "version_requested": "2.0.0",
      "comparator": "=",
      "unknown": False,
      "outdated": True,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://opensource.org/licenses/mit-license.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "capybara-webkit",
      "prod_key": "capybara-webkit",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "1.14.0",
      "version_requested": "1.11.1",
      "comparator": "=",
      "unknown": False,
      "outdated": True,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://spdx.org/licenses/MIT.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "climate_control",
      "prod_key": "climate_control",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "0.2.0",
      "version_requested": "0.0.3",
      "comparator": "=",
      "unknown": False,
      "outdated": True,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "https://raw.githubusercontent.com/thoughtbot/climate_control/master/LICENSE.txt",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "cocaine",
      "prod_key": "cocaine",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "0.5.8",
      "version_requested": "0.5.8",
      "comparator": "=",
      "unknown": False,
      "outdated": False,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://spdx.org/licenses/MIT.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "coffee-rails",
      "prod_key": "coffee-rails",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "4.2.2",
      "version_requested": "4.2.1",
      "comparator": "=",
      "unknown": False,
      "outdated": True,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://spdx.org/licenses/MIT.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
    {
      "name": "coffee-script",
      "prod_key": "coffee-script",
      "group_id": None,
      "artifact_id": None,
      "language": "ruby",
      "scope": "compile",
      "version_current": "2.4.1",
      "version_requested": "2.4.1",
      "comparator": "=",
      "unknown": False,
      "outdated": False,
      "stable": True,
      "licenses": [
        {
          "name": "MIT",
          "url": "http://spdx.org/licenses/MIT.html",
          "on_whitelist": True,
          "on_cwl": None
        }
      ],
      "security_vulnerabilities": None
    },
  ],
  "child_ids": [],
  "parent_id": None
}

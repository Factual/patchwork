from datetime import datetime, timedelta, timezone
import time

def current_time():
    return time.time()

'''
Parses the timestamps in the VersionEye json responses
Returns date object in local timezone
'''
def convert_versioneye_timestamp(time_string):
    date_template = "%Y-%m-%dT%H:%M:%S"
    time_string = time_string.split('.')[0]
    if not 'T' in time_string:
        date_template = date_template.split('T')[0]

    local_timezone = datetime.now(timezone.utc).astimezone().tzinfo
    utc_time = datetime.strptime(time_string, date_template)
    local_time = utc_time.replace(tzinfo=timezone.utc).astimezone(local_timezone)
    return time.mktime(local_time.timetuple())

'''
Given a file path, replaces the absolute path to the top level directory
with the name of that directory as specified in the config file

Eg: fname '/Absolute/Path/to/repo_name/file.type' with
directory = '/Absolute/Path/to/repo_name' and directory_name = 'repo_name'
would return 'repo_name/file.type'
'''
def get_display_name(fname, params):
    return fname.replace(params['directory'], params['directory_name'])

'''
Gets date string to be used as folder name for persisting reports
'''
def get_datetime():
    return datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d--%H_%M')

'''
mm-dd-yy timestamp from epoch timestamp (seconds param)
'''
def date_string(seconds):
    t = datetime.fromtimestamp(seconds)
    return t.strftime("%m-%d-%Y")

'''
:param ts: epoch timestamp (int)
True iff ts within 2 weeks of current time
'''
def within_last_sprint(ts):
    now = datetime.fromtimestamp(time.time())
    then = datetime.fromtimestamp(ts)
    total_time = now - then
    SPRINT_LENGTH = 2
    sprint = timedelta(weeks=SPRINT_LENGTH)
    return total_time < sprint

'''
True iff only last bit of version numbers are different
Assumes available version is more recent or equivalent to 'ours'

:param ours: Version specified by dependency file
:param available: Current version of that dependency

eg if ours = 1.2.0, available = 1.2.2 would be true
but available = 1.3.0 or higher would be false
'''
def minor_release(ours, available):
    return ours.startswith('.'.join(available.split('.')[:-1])) and ours != available

'''
True iff first bit of version numbers are different
Assumes available version is more recent or equivalent to 'ours'

:param ours: Version specified by dependency file
:param available: Current version of that dependency

eg if ours = 1.2.0, available = 2.0 or higher would be true,
all else would be false
'''
def major_release(ours, available):
    return ours.split('.')[0] != available.split('.')[0]

'''
True iff first bit of version numbers are same but more than the last bit differs
- essentially, neither a major nor a minor release
Assumes available version is more recent or equivalent to 'ours'

:param ours: Version specified by dependency file
:param available: Current version of that dependency

eg if ours = 1.2.0, 1.3 <= available < 2.0 would be true,
all else would be false
'''
def other_release(ours, available):
    return ours != available

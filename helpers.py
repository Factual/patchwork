from datetime import datetime, timedelta
import time, pytz, tzlocal

def convert_versioneye_timestamp(time_string):
    date_template = "%Y-%m-%dT%H:%M:%S"
    time_string = time_string.split('.')[0]
    if not 'T' in time_string:
        date_template = date_template.split('T')[0]

    local_timezone = tzlocal.get_localzone()
    utc_time = datetime.strptime(time_string, date_template)
    local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
    return time.mktime(local_time.timetuple())

def get_display_name(fname, params):
    return fname.replace(params['directory'], params['report_directory'])

def get_datetime():
    return datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d--%H_%M')

def within_last_sprint(ts):
    now = datetime.fromtimestamp(time.time())
    then = datetime.fromtimestamp(ts)
    total_time = now - then
    sprint = timedelta(weeks=2)
    return total_time < sprint

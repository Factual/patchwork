from datetime import datetime
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

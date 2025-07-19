import datetime
import pytz

def convertToDiscordTimestamp(time_string):
    time_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    time_object = datetime.datetime.strptime(time_string, time_format)
    local_timezone = pytz.timezone('Australia/Melbourne')
    localized_time = local_timezone.localize(time_object)
    timestamp = f'<t:{int(localized_time.timestamp())}:R>'
    return timestamp
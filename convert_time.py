
import datetime


def convert_time(time_array):
    human_time = []
    for time in time_array:
        convert = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
        human_time.append(convert)
    return human_time


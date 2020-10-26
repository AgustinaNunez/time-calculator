def get_day_name(start_day_name, days_later):
    days_name = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if start_day_name != '':
        day_index = days_name.index(start_day_name.lower()) + days_later
        if days_later > 6:
            day_index %= 7
        return days_name[day_index]


def add_time(start, duration, start_day_name=''):
    # split data
    start_meridian = start.split()[1]
    start_hours = int(start[:-3].split(":")[0])
    start_minutes = int(start[:-3].split(":")[1])
    duration_hours = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])

    # get minutes
    minutes = start_minutes + duration_minutes
    minutes_hours = 0
    if minutes >= 60:
        minutes, minutes_hours = minutes % 60, minutes // 60

    # get hours
    hours = start_hours + duration_hours + minutes_hours
    days_later = 0

    # to 24 hours-format
    if start_meridian == 'PM':
        hours += 12
    if hours >= 24:
        hours, days_later = hours % 24, hours // 24

    # to 12 hours-format
    meridian = 'PM' if hours >= 12 else 'AM'
    if hours > 12:
        hours -= 12
    if hours == 0:
        hours = 12

    day_name = get_day_name(start_day_name, days_later)

    # build result
    new_time = f'{hours}:{minutes:02d} {meridian}'
    if start_day_name != '':
        new_time += f', {day_name.capitalize()}'
    if days_later == 1:
        new_time += ' (next day)'
    elif days_later > 1:
        new_time += f' ({days_later} days later)'
    return new_time

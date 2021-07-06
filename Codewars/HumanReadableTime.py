import math
def make_readable(seconds):
    hours = math.floor(seconds / 3600)
    seconds = seconds % 3600
    minutes = math.floor(seconds / 60)
    seconds = seconds % 60

    if len(str(hours)) < 2:
        if len(str(hours)) == 1:
            hours = f'{0}{hours}'
    if len(str(minutes)) < 2:
        if len(str(minutes)) == 1:
            minutes = f'{0}{minutes}'
    if len(str(seconds)) < 2:
        if len(str(seconds)) == 1:
            hours = f'{0}{seconds}'
    return f'{hours}:{minutes}:{seconds}'

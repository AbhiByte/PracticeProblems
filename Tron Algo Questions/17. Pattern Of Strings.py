def func(string1, string2):
    pattern = {}
    for a, b in zip(string1, string2.split()):
        pattern.setdefault(a, b)
    for x, y in zip(string1, string2.split()):
        if pattern[x] != y:
            return False
    return True

def increment_string(string):
    num = []
    for item in string:
        if item.isnumeric() == True and int(item) != 0:
            num.append(item)
            string = string.replace(item, '')
    new_num = 1 + int(''.join(num))
    new_string = ''.join((string, str(new_num)))
    return new_string

print(increment_string('foobar036'))

def first_non_repeating_letter(string):
    dict = {}
    for s in string.upper().replace(" ", ''):
        dict.setdefault(s, 0)
        dict[s] += 1
    for x in dict:
        if dict[x] == 1:
            for char in string:
                if x.upper() == char or x.lower() == char:
                    return char
    return ''

print(first_non_repeating_letter('sTreSS'))

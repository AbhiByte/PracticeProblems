#Q8. Very easy using dictionary.
def unique(string):
    count = {}
    for x in string.lower():
        count.setdefault(x, 0)
        count[x] += 1
    for vals in count.values():
        if vals != 1:
            return "Not Unique"
    return "Unique"

print(unique("Mr. Fancy Pants"))

import itertools

def isIsomorphic(s, t):
    letters = {}
    for (x,y) in zip(s,t):
        if x not in letters.keys():
            for key, value in letters.items():
                if key == x and value == y:
                    letters.setdefault(x,y)
    print(letters)
    rev_multidict = {}
    for key, value in letters.items():
        rev_multidict.setdefault(value, set()).add(key)
    x = [key for key, values in rev_multidict.items() if len(values) > 1]
    print(x)
    if x == []:
        return True
    else:
        return False



print(isIsomorphic('foo', 'bar'))

import itertools

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    pairs = {}
    used = {}

    for i in range(len(s)):
        char1 = s[i]
        char2 = t[i]
        if char1 in pairs.keys():
            if pairs[char1] != char2:
                return False
        else:
            if used[char2] == True:
                return False
            else:
                pairs[char1] = char2
                used[char2] = True




print(isIsomorphic('egg', 'add'))

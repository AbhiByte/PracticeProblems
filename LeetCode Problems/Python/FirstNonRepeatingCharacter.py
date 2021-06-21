#Going to use dictionary to get O(n) time
#Given a string find the first non repeating character

def answer(string, map={}):
    #Creates dictionary
    for x in string:
        map[x] = map.setdefault(x, 0) + 1
    #Searches dictionary for character with 'character' : 1
    for x in map:
        if map[x] == 1:
            return x
    #return map
print(answer("aaabcbbcefff"))

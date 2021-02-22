def romanToInt(s):
    total = 0
    for x in (s):
        if x == "I":
            total += 1
        elif x == "V":
            total += 5
        elif x == "X":
            total += 10
        elif x == "L":
            total += 50
    return total


s = "IX"
print(romanToInt(s))

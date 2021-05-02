def kidsWithCandies(candies, extraCandies):
    length = len(candies)
    boolCandy = [None]*length
    maxVal = 0
    for x in range(length):
        if candies[x] > maxVal:
            maxVal = candies[x]
    for i in range(length):
        if candies[i] + extraCandies >= maxVal:
            boolCandy[i] = True
        else:
            boolCandy[i] = False
    return boolCandy

list = [12,1,12]
num = 10
print(kidsWithCandies(list, num))

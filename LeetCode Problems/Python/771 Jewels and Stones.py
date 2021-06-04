#Complexity could be improved
#For each element in stones checks to see if element in jewels also in stones and ++ the counter
def numJewelsInStones(jewels, stones):
    counter = 0
    for x in stones:
        for i in jewels:
            if i == x:
                counter += 1
    return counter

jewels = "z"
stones = "ZZ"
ans = numJewelsInStones(jewels, stones)
print (ans)

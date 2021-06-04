def maximumWealth(accounts):
    length = len(accounts)
    sum = 0
    ans = 0
    for x in range (length):
        for y in range (len(accounts[x])):
            sum += accounts[x][y]
        if sum > ans:
            ans = sum
        sum = 0
    return ans
account = [[2,8,7],[7,1,3],[1,9,5]]
print(maximumWealth(account))

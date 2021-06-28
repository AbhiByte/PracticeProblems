
def climb(n, count = 0):
    if n > 1:
        return count
    else:
        return climb(n-1, count + 1)




print(climb(5))

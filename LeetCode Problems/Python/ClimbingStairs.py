
def climb(n, count = {}):
    if n in count:
        return count[n]
    if n <= 1:
        return 1
    count[n] = climb(n-1, count) + climb(n-2, count)
    return count[n]





print(climb(2))

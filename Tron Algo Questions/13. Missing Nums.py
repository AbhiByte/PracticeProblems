#Q11 O(n) time where n is max value
def missing(arr):
    MAX = max(arr)
    count = min(arr)
    ans = []
    for x in range(MAX):
        if count not in arr:
            ans.append(count)
        count+=1
    return ans

print(missing([1,3,5]))

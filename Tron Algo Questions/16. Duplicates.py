#Linear time for first loop and dict lookup is constant
def find_duplicates(arr):
    counter = {}
    for x in arr:
        counter.setdefault(x, 0)
        counter[x] += 1
    ans = []
    for keys in counter.keys():
        if counter[keys] >= 2:
            ans.append(keys)
    return ans
print(find_duplicates([1,1,2,2,4]))

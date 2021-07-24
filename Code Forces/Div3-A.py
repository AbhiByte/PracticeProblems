import math
n = int(input())
arr = []
for x in range(0, n):
    num = int(input())
    arr.append(num)
def find(arr):
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            return abs(arr[x][y-1] - arr[x][y])
for nums in arr:
    if nums == 1:
        print(1, 0)
        continue
    combos = []
    for x in range(nums):
        for y in range(nums):
            if x + 2*y == nums:
                combos.append([x, y])

    w = min(combos, key = lambda x: abs(x[0] - x[1]))
    print(w)

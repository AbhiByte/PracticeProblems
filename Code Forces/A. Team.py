n = int(input())
inputs = []
for x in range(n):
    a, b, c = int(input()).split()
    inputs.append([a, b, c])
total = 0
for nums in inputs:
    if sum(nums) == 2 or sum(nums) == 3:
        total+=1

print(total)

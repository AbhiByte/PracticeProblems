n = int(input())
inputs = []
for x in range(n):
    a, b, c = input().split()
    inputs.append([a, b, c])
count = 0
for nums in inputs:
    total = 0
    for x in nums:
        total += int(x)
    if total == 2 or total == 3:
        count += 1

print(count)

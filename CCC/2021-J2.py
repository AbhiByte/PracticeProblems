n = int(input())
arr = []
for x in range(0, n):
    name = str(input())
    bid = int(input())
    arr.append([name, bid])

max_value = max([sublist[-1] for sublist in arr])


duplicates = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == max_value:
            duplicates.append(arr[i][j-1])

print(duplicates[0])

def find_even_index(arr):
    for i in range(len(arr)):
        left = 0
        right = 0
        for x in range(i):
            left += arr[x]
        for y in range(i+1, len(arr)):
            right += arr[y]
        if left == right:
            return i
    return -1




print(find_even_index([1, 2, 3, 4, 3, 2, 1]))

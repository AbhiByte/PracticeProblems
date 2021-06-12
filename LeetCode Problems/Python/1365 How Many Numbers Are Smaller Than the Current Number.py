def func(input):
    ans = []
    for x in input:
        temp_count = 0
        for y in range(1, len(input)+1):
            if input[y] < x:
                temp_count += 1
            ans.append(temp_count)
    return ans

print(func([8,1,2,2,3]))

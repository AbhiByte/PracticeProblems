def func(input):
    ans = []
    for x in range(len(input)):
        temp_ans = 0
        for y in range(len(input)):
            if x != y:
                if input[x] > input[y]:
                    temp_ans += 1

        ans.append(temp_ans)

    return ans

print(func([8,1,2,2,3]))

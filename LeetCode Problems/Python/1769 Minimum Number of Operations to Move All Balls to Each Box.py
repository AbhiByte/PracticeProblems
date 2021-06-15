def minOperations(boxes):
    ans = []
    #Right side, Left side
    for x in range(len(boxes)):
        right_count, left_count = 0, 0
        for y in range(len(boxes) + 1):
            if boxes[x] == '1':
                right_count += (y-x)

        for y in range(x-1):
            if y > -1 and y != x:
                left_count += (x-y)


        ans.append(right_count+left_count)
    return ans



boxes = "110"
print(minOperations(boxes))



"""
expected ans: [1, 1, 3]
1 move to move all balls to box 1. 1 move to move all balls to box 2
3 moves to move all balls to box 3
"""

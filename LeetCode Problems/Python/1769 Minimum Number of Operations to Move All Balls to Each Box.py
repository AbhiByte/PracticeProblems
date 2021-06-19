def minOperations(boxes):

    ans = []
    for x in range(len(boxes)):
        #Left side
        left_counter = 0
        for l in range(len(boxes)):
            if l < x:
                if boxes[l] == '1':
                    left_counter += (x - l)
        #Right side
        right_count = 0
        for r in range(len(boxes)):
            if r > x:
                if boxes[r] == '1':
                    right_count += (r - x)
        ans.append((left_counter+right_count))
    return ans


boxes = "110"
print(minOperations(boxes))



"""
expected ans: [1, 1, 3]
1 move to move all balls to box 1. 1 move to move all balls to box 2
3 moves to move all balls to box 3
"""

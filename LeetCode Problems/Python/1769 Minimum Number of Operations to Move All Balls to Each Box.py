def minOperations(boxes):
        ans = map(int, boxes)
        print(list(ans)[0])


boxes = "110"
minOperations(boxes)



"""
expected ans: [1, 1, 2]
1 move to move all balls to box 1. 1 move to move all balls to box 2
2 moves to move all balls to box 3
"""

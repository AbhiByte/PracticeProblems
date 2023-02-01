'''Slightly buggy solution'''
import math
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0])
        while l <= r:
            mid = (l+r)//2 
            mid_row = math.floor(mid/len(matrix[0]))
            mid_col = mid%len(matrix[0])

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                l = mid+1
            else:
                r = mid-1
        return False
 

'''Complete solution'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1
        while lo <= hi:
            midRow = (lo + hi) // 2
            row = matrix[midRow]
            if target < row[0]: hi = midRow - 1
            elif target > row[-1]: lo = midRow + 1
            else:
                l, h = 0, len(row) - 1
                while l <= h:
                    mid = (l + h) // 2
                    if row[mid] == target: return True
                    elif target > row[mid]: l = mid + 1
                    else: h = mid - 1
                return False
#O(log m + log n)

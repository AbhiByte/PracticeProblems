'''
Runtime: 20 ms, faster than 78.19% of Python online submissions for Valid Perfect Square.
Memory Usage: 13.4 MB, less than 61.47% of Python online submissions for Valid Perfect Square.
'''

class Solution(object):
    def isPerfectSquare(self, num):
        l, r = 0, num
        while l<=r:
            mid = (l+r)//2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                r = mid-1
            elif mid**2 < num:
                l = mid+1
        return False

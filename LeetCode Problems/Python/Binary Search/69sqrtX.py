'''
Brute force solution. Worst case O(n). 

Runtime: 3073 ms, faster than 8.16% of Python online submissions for Sqrt(x).
Memory Usage: 13.3 MB, less than 61.54% of Python online submissions for Sqrt(x).
'''
class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0
        if x == 1:
            return 1
        if x == 2:
            return 1
        count = 1
        while count < x:
            if count*count > x:
                return count - 1
            else:
                count += 1
                
'''
Binary Search Implementation

Runtime: 37 ms, faster than 56.81% of Python online submissions for Sqrt(x).
Memory Usage: 13.3 MB, less than 83.06% of Python online submissions for Sqrt(x).
'''

def mySqrt(self, x):
         
        lo, hi = 0, x
        if x == 1: 
            return 1 
        
        while lo <= hi:
            mid = (lo+hi)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                hi = mid -1
            else:
                lo = mid + 1
      
    
     
        

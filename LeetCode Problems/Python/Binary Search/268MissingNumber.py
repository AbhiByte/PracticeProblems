'''
Quick implementation

Runtime: 100 ms, faster than 98.01% of Python online submissions for Missing Number.
Memory Usage: 14.7 MB, less than 43.72% of Python online submissions for Missing Number.
'''

class Solution(object):
    def missingNumber(self, nums):
        required_sum = (len(nums) * (len(nums) + 1))/2
        return required_sum - sum(nums)

      
      
 '''
 Binary Search Implementation
 
 '''



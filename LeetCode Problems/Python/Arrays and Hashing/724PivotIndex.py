class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        l, r = 0, sum(nums)
        
        for index, num in enumerate(nums):
            r -= num
            if l == r:
                return index
            l+=num
        return -1
      
      
      
      
# Runtime: 140 ms, faster than 99.78% of Python3 online submissions for Find Pivot Index.
# Memory Usage: 15.3 MB, less than 11.20% of Python3 online submissions for Find Pivot Index.

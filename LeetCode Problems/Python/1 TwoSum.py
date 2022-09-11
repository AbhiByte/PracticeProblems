# 1. Two Sum
def twoSum(nums, target):
    list = []
    for i in range (len(nums) - 1):
        for j in range (i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
            
            
            
            
#NeetCode solution (hashmap)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevVal = {} # Val : Index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevVal:
                return [prevVal[diff], i]
            prevVal[n] = i

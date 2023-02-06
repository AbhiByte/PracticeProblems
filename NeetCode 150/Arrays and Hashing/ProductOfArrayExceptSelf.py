'''Solution that works but doesnt pass on LC due to runtime error'''
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        for i in range(len(nums)):
            prefix_temp = [num for num in nums[:i]]
            postfix_temp = [num for num in nums[i+1:]]
            output[i] = math.prod(prefix_temp) * math.prod(postfix_temp)
        return output
      
      

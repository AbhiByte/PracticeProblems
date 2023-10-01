"""Solution that works but doesnt pass on LC due to runtime error"""
import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i in range(len(nums)):
            prefix_temp = [num for num in nums[:i]]
            postfix_temp = [num for num in nums[i + 1 :]]
            output[i] = math.prod(prefix_temp) * math.prod(postfix_temp)
        return output


"""Neetcode solution Early 2023"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


"""Fall 2023 I had the same solution as above. O(2n) since 2 passes through array"""

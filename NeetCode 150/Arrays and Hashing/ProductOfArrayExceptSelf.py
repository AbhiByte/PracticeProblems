"""Solution that works but doesnt pass on LC due to runtime error"""
import math


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = [1] * len(nums)
        for i in range(len(nums)):
            prefix_temp = [num for num in nums[:i]]
            postfix_temp = [num for num in nums[i + 1 :]]
            output[i] = math.prod(prefix_temp) * math.prod(postfix_temp)
        return output


"""Neetcode solution Early 2023"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
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


# Summer 2024 solution
def productExceptSelf(nums: list[int]) -> list[int]:

        left = [1]*len(nums)
        prod = 1
        for i, num in enumerate(nums[:len(nums)-1]):
            prod *= num
            left[i+1] = prod

        prod = 1
        right = [1]*len(nums)

        for i, num in enumerate(nums[::-1]):
            prod *= num
            right[len(nums) - i - 2] *= prod
            right[-1] = 1

        return [l*r for l, r in zip(left, right)]

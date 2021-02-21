# 1. Two Sum
def twoSum(nums, target):
    list = []
    for i in range (len(nums) - 1):
        for j in range (i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j

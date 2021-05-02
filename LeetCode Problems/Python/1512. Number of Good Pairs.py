def good (nums):
    ans = 0
    for x in range(len(nums)):
        for y in range(len(nums)):
            if x < y and nums[x] == nums[y]:
                ans+=1
    return ans
nums = [1,2,3]
print(good(nums))

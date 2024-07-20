# My solution. Works but runtime error :/
def twoSum(nums, target, index3sum):
    result = []
    prevMap = {}  # val -> index
    for i, n in enumerate(nums):
        if i != index3sum:
            diff = target - n
            if diff in prevMap:
                result.append([prevMap[diff], i])
            prevMap[n] = i
    return result


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sol = []
        for i in range(len(nums)):
            target = -nums[i]
            newlist = nums[:i] + nums[i + 1 :]
            twoSumResult = twoSum(nums, target, i)
            # print(f"nums[{i}]: {nums[i]}, target: {target}, newlist: {newlist}, twoSumResult: {twoSumResult}")
            if twoSumResult != None:
                for lst in twoSumResult:
                    sol.append([nums[i]] + [nums[lst[0]]] + [nums[lst[1]]])

        seen = []
        for lst in sol:
            if sorted(lst) not in seen:
                seen.append(sorted(lst))
        return seen


# Fall 2023 solution (not mine)
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    output = []

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:  # if repeat number, move on
            continue

        l, r = i + 1, len(nums) - 1  # conduct 2 sum II on the remaining list

        while l < r:
            three_sum = a + nums[l] + nums[r]

            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                output.append([a, nums[r], nums[l]])

                l += 1  # while repeat num, move left pointer (or we could move right pointer)
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return output


# Summer 2024 solution (still don't understand this too well. come back)
def threeSum(self, nums: list[int]) -> list[list[int]]:

        ans = []
        nums.sort()

        for i, num in enumerate(nums):

            if i > 0 and num == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = num + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return ans

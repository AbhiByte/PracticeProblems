#My solution. Works but runtime error :/
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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        for i in range(len(nums)):
            target = -nums[i]
            newList = nums[:i] + nums[i+1:]
            twoSumResult = twoSum(nums, target, i)
            #print(f"nums[{i}]: {nums[i]}, target: {target}, newList: {newList}, twoSumResult: {twoSumResult}")
            if twoSumResult != None:
                for lst in twoSumResult:
                    sol.append([nums[i]] + [nums[lst[0]]] + [nums[lst[1]]])
        
        seen = []
        for lst in sol:
            if sorted(lst) not in seen:
                seen.append(sorted(lst))
        return seen

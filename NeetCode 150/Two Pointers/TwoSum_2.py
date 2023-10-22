# Medium problem similar to TwoSum but index+1
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        output = []
        val_index = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in val_index.keys():
                return [val_index[diff] + 1, i + 1]
            else:
                val_index.setdefault(numbers[i], i)


# Fall 2023 solution
# Time complexity O(n), space complexsity constant
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                break
            elif curr_sum < target:
                l += 1
            else:
                r -= 1

        return sorted([l + 1, r + 1])

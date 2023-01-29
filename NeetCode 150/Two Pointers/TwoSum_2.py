#Medium problem similar to TwoSum but index+1
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        val_index = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in val_index.keys():
                return [val_index[diff] + 1, i+1]
            else:
                val_index.setdefault(numbers[i], i)

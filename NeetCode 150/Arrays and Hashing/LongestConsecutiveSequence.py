#My solution. Run O(n) since at most one iteration through nums. Uses set which adds memory
def remove_duplicates(l):
    return list(set(l))
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = remove_duplicates(nums)
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        count = 1
        seq = []
        l = 0
        r = 1
        while l<len(nums)-1:
            if nums[r] == nums[l] + 1:
                count+=1
                l+=1
                r+=1
            else:
                seq.append(count)
                count = 1
                l=r
                r+=1
        seq.append(count)     
        return max(seq)

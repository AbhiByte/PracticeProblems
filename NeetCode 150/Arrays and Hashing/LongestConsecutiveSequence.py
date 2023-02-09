#My solution. Run O(n) since at most one iteration through nums. Uses set which adds memory

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums)).sort()
        if len(nums) == 0:
            return 0
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
    
    
    #NC Soluton. Linear time, memory. Similar to mine but uses exact value instead of index
    class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

'''Runtime: 1445 ms, faster than 5.03% of Python3 online submissions for Contains Duplicate.
Memory Usage: 25.8 MB, less than 96.46% of Python3 online submissions for Contains Duplicate.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occur = {}
        for x in nums:
            occur.setdefault(x, 0)
            occur[x] += 1
        
        for keys in occur.keys():
            if occur[keys] >= 2:
                return True
        return False

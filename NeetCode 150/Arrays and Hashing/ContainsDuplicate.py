class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            count.setdefault(num, 0)
            count[num] += 1
        
        for key, value in count.items():
            if value >= 2:
                return True
        return False
 

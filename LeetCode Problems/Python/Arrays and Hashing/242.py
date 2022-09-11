'''Runtime: 56 ms, faster than 84.50% of Python3 online submissions for Valid Anagram.
Memory Usage: 15.8 MB, less than 12.03% of Python3 online submissions for Valid Anagram.'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        #Method 1 -> sorting
        ls = [char for char in s]
        a = sorted(ls)
  

        lt = [char for char in t]
        b = sorted(lt)

        if a==b:
            return True
        return False
 

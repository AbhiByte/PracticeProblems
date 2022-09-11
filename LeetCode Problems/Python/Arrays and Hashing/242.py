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

'''Runtime: 111 ms, faster than 13.70% of Python3 online submissions for Valid Anagram.
Memory Usage: 15.2 MB, less than 12.03% of Python3 online submissions for Valid Anagram.'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        #Method 2 -> Hashing
        count1 = {}
        count2 = {}
        ls = [char for char in s]
        lt = [char for char in t]
        
        for x in ls:
            count1.setdefault(x, 0)
            count1[x] += 1
        
        for x in lt:
            count2.setdefault(x, 0)
            count2[x] += 1
        
        if count1 == count2:
            return True
        return False
 

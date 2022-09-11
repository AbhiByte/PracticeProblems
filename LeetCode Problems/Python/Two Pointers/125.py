Runtime: 98 ms, faster than 24.71% of Python3 online submissions for Valid Palindrome.
Memory Usage: 15.1 MB, less than 29.41% of Python3 online submissions for Valid Palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = ''.join(e for e in s if e.isalnum())
        if s == s[::-1]:
            return True
        return False

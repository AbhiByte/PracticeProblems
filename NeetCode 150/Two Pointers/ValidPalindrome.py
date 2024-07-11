class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch for ch in s if ch.isalnum()).lower()
        return s == s[::-1]


# Fall 2023 solution.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        for char in s:
            if char.isalnum() == False:
                s = s.replace(char, "")
        return s.lower() == s[::-1].lower()
    
    
    
# Summer 2024 solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()


        # O(n/2) = O(n)
        for i in range((len(s) + 1) // 2):  # Only need to go halfway
            front_char = s[i]
            back_char = s[-(i + 1)]

            if front_char != back_char:
                return False
        
        return True
                
        

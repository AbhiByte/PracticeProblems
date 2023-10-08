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

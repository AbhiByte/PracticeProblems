'''O(n) runtime since O(n) loop and O(26) (max) dictionary'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letterCount = {}
        l = 0
        maxCount = 0
        maxLetter = 0
        for r in range(len(s)):
            letterCount.setdefault(s[r], 0)
            letterCount[s[r]] += 1

            maxLetter = max(maxLetter, letterCount[s[r]])

            if r-l+1 - maxLetter > k:
                letterCount[s[l]] -= 1
                l += 1
            maxCount = max(maxCount, r-l+1)
        return maxCount

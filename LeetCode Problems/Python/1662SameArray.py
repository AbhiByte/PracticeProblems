class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        new_s1 = ''.join(word1)
        new_s2 = ''.join(word2)
        if new_s1 == new_s2:
            return True
        return False

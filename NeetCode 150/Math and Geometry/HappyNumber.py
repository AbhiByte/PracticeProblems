'''
36 ms
Beats
76.11%
Memory
13.7 MB
Beats
99.94%
'''
class Solution:
    def isHappy(self, n: int) -> bool:

        seen = []
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in seen:
                return False
            seen.append(n)
        return True

#Recursive solution with @cache
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
      
      
      
#Neetcode solution:
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2

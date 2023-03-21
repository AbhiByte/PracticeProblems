#O(n) solution since we iterate through n times for each k
#Since k ∝ n, it's actually O(n^2)
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_max = max(piles)
    
        for k in range(1, k_max+1):
            total_hours = 0
        
            for p in piles:
                total_hours += math.ceil(p/k)
            if total_hours <= h:
                return k
              
              
#We can reduce k search from O(k) to O(log k) by using binary search
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_min = 1
        k_max = max(piles)
        output = max(piles)
    
        while k_min <= k_max:
            k = (k_min + k_max) // 2
            total_hours = 0
        
            for p in piles:
                total_hours += math.ceil(p/k)
            if total_hours > h:
                k_min = k + 1
            if total_hours <= h:
               output = k
               k_max = k - 1
        return output

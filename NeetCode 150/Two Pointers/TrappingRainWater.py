#O(n^2) brute force solution
class Solution:
    def trap(self, height: List[int]) -> int:
        #min of max h of bars on both sides minus its own height

        water = 0
        for i in range(1, len(height)-1):
            calc = min(max(height[:i]), max(height[i+1:])) - height[i]
            if calc > 0:
                water += calc
        return water
      
#optimal Solution

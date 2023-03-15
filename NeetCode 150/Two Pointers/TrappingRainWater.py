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
      
#optimal Solution (with help from NC)
#O(n) time and constant space. Revisit after some time for refresher 
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        output = 0

        while l < r:
            if maxLeft < maxRight:
                l+=1
                maxLeft = max(maxLeft, height[l])
                output += maxLeft - height[l]
            
            else:
                r-=1
                maxRight = max(maxRight, height[r])
                output += maxRight - height[r]
            
        return output

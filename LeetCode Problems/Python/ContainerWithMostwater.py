import math
class Solution(object):
    def maxArea(self, height):
        area = 0
        for x in range(len(height)):
            for y in range(1, len(height)):
                if min(height[x], height[y]) * (y-x)> area:
                    area = min(height[x], height[y]) * (y-x)
        return area

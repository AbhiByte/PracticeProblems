# My solution
class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea = 0

        l, r = 0, len(height) - 1
        while l < r:
            area = min(height[r], height[l]) * (r - l)
            maxArea = max(maxArea, area)

            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        return maxArea


# Fall 2023 Solution
class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            area = (r - l) * min(height[r], height[l])

            maxArea = max(area, maxArea)

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxArea

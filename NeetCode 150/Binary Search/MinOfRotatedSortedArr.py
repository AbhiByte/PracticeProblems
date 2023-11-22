class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # We know initially l > r because it is rotated
        minimum = nums[0]
        while l <= r:
            mid = (l + r) // 2
            minimum = min(minimum, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return min(minimum, nums[l])


# My Fall 2023 solution
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid] <= nums[r]:
                return nums[l]
            elif nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid

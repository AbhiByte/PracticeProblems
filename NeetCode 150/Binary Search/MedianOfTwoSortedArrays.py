#My solution beats 95% in memory but it slow
import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = sorted(nums1+nums2)
    
        if len(merge) % 2 != 0:
            return merge[math.floor(len(merge) / 2)]
        return (merge[math.floor(len(merge) / 2)] + merge[math.floor(len(merge) / 2) - 1])/2

#Hard problem
def findMedianSortedArrays(nums1, nums2):
    arr = sorted(nums1 + nums2)
    length = len(arr)
    if length%2 == 0:
        ans = (arr[int(length/2)] + arr[int(length/2)-1]) / 2
        return ans
    else:
        ans = arr[int(length/2)]
    return ans

print(findMedianSortedArrays([1, 2], [3, 4]))

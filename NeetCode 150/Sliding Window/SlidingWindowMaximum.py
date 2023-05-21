#Valid solution but slow so doesnt pass LC. Is O(n) since one iteration and max() is O(k) 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Base case
        if k == 1:
            return nums
        
        #Init some variables
        l = 0
        r = k-1
        maxCount = []
        currMax = 0
        counter = 0
        #Loop through all windows of size k
        while r <= len(nums)-1:
            counter += 1
            if l == 0 and r == k-1:
                currMax = max(nums[l:r+1])
                maxCount.append(currMax)
            else:

                if nums[r] > currMax:
                    currMax = nums[r]
                    maxCount.append(currMax)
                else:
                    #if not then 2 possibilities
                    if nums[l-1] == currMax:
                        currMax = max(nums[l:r+1])
                        maxCount.append(currMax)
                    else:
                        maxCount.append(currMax)
            r += 1
            l += 1
            
        
        return maxCount
 
#Optimized solution

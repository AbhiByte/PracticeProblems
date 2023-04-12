#Very slow due to sorted at each step. O(n) windows and then sorted is O(n) best case so O(n^2) best case and O(n^2 log n) average

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Window size
        left, right = 0, len(s1)-1
                
        while right < len(s2):
            temp = s2[left:right+1]
            if sorted(temp) == sorted(s1):
                return True
            else:
                left += 1
                right +=1
        return False

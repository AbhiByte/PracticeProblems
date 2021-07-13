class Solution(object):
    def plusOne(self, digits):
        ans = []
        for x in (str(int("".join([str(integer) for integer in digits])) + 1)):
            ans.append(x)
        return ans
        

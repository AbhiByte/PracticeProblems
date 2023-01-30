class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        out = []
        num = int("".join(str(i) for i in digits))
        num+=1
        for x in str(num):
            out.append(int(x))
        return out

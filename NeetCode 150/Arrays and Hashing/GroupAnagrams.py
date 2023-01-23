#Buggy code haha
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        out = []
        #count number of occurances of each letter in each string
        for s in strs:
            sorted_s = "".join(sorted(s))
            result.setdefault(sorted_s, [s])
            result[sorted_s] += [s]
        for key in result.keys():
            out.append(result[key])
        for x in out:
            x.pop(0)
        return out

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
    
    
'''* Much better cleaner solution. Runtime 85ms Beats 99.54%, Memory 17.1MB Beats 86.23% *'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        #count number of occurances of each letter in each string
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in result.keys():
                result.setdefault(sorted_s, [s])
            else:
                result[sorted_s] += [s]
        return [x for x in result.values()]


'''Neetcode solution O(m * n)'''
class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord('a')] += 1 #essentially count occurance of each letter
            
            res[tuple(count)].append(s) #then for that specific occurance list, add the string associated with it

        return res.values()

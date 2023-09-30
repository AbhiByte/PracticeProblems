#Probably very inefficient but my solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        abs_max_val = abs(max(nums, key=abs))
        count = [0] * (1+ 2*abs_max_val)
        for x in nums:  
            count[abs_max_val + x]+=1 
        count2 = sorted(count)[-k:][::-1]
        tracker = 0
        while tracker < len(count2):
            for index, freq in enumerate(count):
                if freq == count2[tracker]:
                    number = index - abs_max_val
                    print(number)
                    output.append(number)
                    if len(output) == k:
                        return output
                    tracker+=1
        return output
        
#Way more efficient O(3n) = O(n) solution
def func(nums, k):
    count = [[] for i in range(len(nums) + 1)]
        hashMap = {} #key, val = num, freq

        for num in nums:
            hashMap.setdefault(num, 0)
            hashMap[num] += 1

        for num, freq in hashMap.items():
            count[freq].append(num)

        return [item for sublist in count for item in sublist if item != None][-k:]

#My solution Fall 2023
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        res = []
        for num in nums: #O(n)
            count.setdefault(num, 0)
            count[num] += 1

        for _ in range(k): #O(k)
            max_val = max(count, key=count.get) #this might be O(n) haha
            res.append(max_val)
            count.pop(max_val)

        return res #O(n) + O(k) + O(n) == O(n)

#Neetcode solution (I think mine is better)
lass Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        res = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for n, c in count.items():
            res[c].append(n)

        output = []
        for i in range(len(res) - 1, 0, -1):
            for n in res[i]:
                output.append(n)
                if len(output) == k:
                    return output


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

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            #Step 1 get 2 heaviest stones
            stones.sort()
            heavy1, heavy2 = stones[-1], stones[-2]

            #Step 2 "smash the together"
            diff = abs(heavy1 - heavy2)
            stones.remove(heavy1)
            stones.remove(heavy2)
            if diff != 0:
                stones.append(diff)
        
        if not stones:
            return 0
        return stones[0]

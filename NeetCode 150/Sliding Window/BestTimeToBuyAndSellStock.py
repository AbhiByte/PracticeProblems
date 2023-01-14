class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1 #Initial window
        maxProfit = 0
        
        while r < len(prices):
            curr = prices[r] - prices[l] #Current price
            if prices[l] < prices[r]:    #If the transanction is +ve
                maxProfit = max(curr, maxProfit) #Take the max of the curr and prev
            else:
                l = r                    #Otherwise, move left window to right
            r += 1                       #And increment right window by 1
        return maxProfit

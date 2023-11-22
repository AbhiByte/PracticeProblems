class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # Initial window
        maxProfit = 0

        while r < len(prices):
            curr = prices[r] - prices[l]  # Current price
            if prices[l] < prices[r]:  # If the transanction is +ve
                maxProfit = max(curr, maxProfit)  # Take the max of the curr and prev
            else:
                l = r  # Otherwise, move left window to right
            r += 1  # And increment right window by 1
        return maxProfit


# Fall 2023 solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            maxProfit = max(maxProfit, (prices[r] - prices[l]))

            if prices[r] <= prices[l]:
                l = r
                r = l + 1
            else:
                r += 1
        return maxProfit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = 1
        maxProfit, profit = 0, 0
        for R in range(len(prices)):
            if prices[R] > prices[L]:
                profit = prices[R] - prices[L]
            else:
                L = R
            maxProfit = max(profit,maxProfit)
        return maxProfit



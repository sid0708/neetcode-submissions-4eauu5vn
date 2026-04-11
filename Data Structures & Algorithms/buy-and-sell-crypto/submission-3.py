class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L =0
        R = 0
        maxProfit = 0
        for R in range(len(prices)):
            if prices[R] > prices[L]:
                profit = prices[R] - prices[L]
                maxProfit= max(profit,maxProfit)
            else:
                L = R
        return maxProfit
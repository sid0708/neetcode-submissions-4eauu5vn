class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = 1
        maxProfit = 0
        for R in range(len(prices)):
            if prices[R] > prices[L]:
                maxProfit = max(maxProfit, prices[R] - prices[L])
            if prices[R] < prices[L]:
                L = R
        return maxProfit



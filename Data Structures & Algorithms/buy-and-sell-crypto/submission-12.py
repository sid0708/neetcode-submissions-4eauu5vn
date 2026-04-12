class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, maxProfit = 0, 0
        L = 0
        for R in range(len(prices)):
            if prices[R] > prices[L]:
                profit = prices[R] - prices[L]
                maxProfit = max(prices[R] - prices[L],maxProfit )
            if prices[R] < prices[L]:
                L = R
        return maxProfit





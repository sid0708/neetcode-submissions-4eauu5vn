class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, maxprofit = 0,0
        L = 0
        for R in range(len(prices)):
            if prices[R] > prices[L]:
                maxprofit = max(maxprofit, prices[R] - prices[L])
            if prices[R] < prices[L]:
                L = R
        return maxprofit




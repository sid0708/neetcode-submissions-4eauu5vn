class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = 0
        #current profit
        profit = 0
        max_profit = 0
        while (R < len(prices)):
            if prices[R] < prices[L]:
                # update buying
                L = R
            if prices[R] > prices[L]:
                profit = prices[R] - prices[L]
            R +=1
            max_profit = max(profit, max_profit)
        return max_profit
        
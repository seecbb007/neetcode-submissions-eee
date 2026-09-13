class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxprofit = 0

        for p in prices:
            profit = p - minp
            maxprofit = max(profit, maxprofit)
            minp = min(minp, p)
        return maxprofit
            
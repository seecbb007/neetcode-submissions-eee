class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float('inf')
        maxprofit = 0

        for p in prices:
            minp = min(minp, p)
            profit = p - minp
            maxprofit = max(maxprofit, profit)
        return maxprofit
        
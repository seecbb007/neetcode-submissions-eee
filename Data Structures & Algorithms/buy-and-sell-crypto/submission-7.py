class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxp = 0

        for p in prices:
            minp = min(minp, p)
            profit = p - minp
            maxp = max(maxp, profit)
        return maxp
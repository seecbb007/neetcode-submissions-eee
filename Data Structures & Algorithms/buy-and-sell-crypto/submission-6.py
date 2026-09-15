class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0
        for p in prices:
            minprice = min(minprice, p)
            profit = p - minprice
            maxprofit = max(maxprofit,profit)
        return maxprofit
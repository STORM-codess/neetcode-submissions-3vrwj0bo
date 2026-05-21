class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        start = prices[0]
        for price in prices:
            profit = max(profit,price - start)
            start = min(start,price)
            
        return profit
        
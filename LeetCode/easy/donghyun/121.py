class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy = 0, inf
        for price in prices:
            buy, profit = min(buy, price), max(profit, price - buy)
        return profit
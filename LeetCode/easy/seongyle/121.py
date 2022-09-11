class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        maxProfit = 0
        i = 0
        j = 1
        
        while j < days:
            candidateProfit = prices[j] - prices[i]
            if (candidateProfit > 0):
                maxProfit = max(maxProfit, candidateProfit)
            else:
                i = j
            j += 1
        return maxProfit
    
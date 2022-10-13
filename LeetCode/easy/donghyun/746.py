class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (1 + len(cost))
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] += min(dp[i-1], dp[i-2]) + cost[i]
        dp[-1] = min(dp[-2], dp[-3])
        return dp[-1]
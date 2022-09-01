import sys
from bisect import bisect_left

input = sys.stdin.readline
n, m = map(int, input().split())
app = list(map(int, input().split()))
cost = list(map(int, input().split()))
dp = [[0] * (1 + sum(cost)) for _ in range(n)]
for i, (a, c) in enumerate(zip(app, cost)):
	for j in range(1 + sum(cost)):
		if j < c:
			dp[i][j] = dp[i - 1][j]
		else:
			dp[i][j] = max(dp[i-1][j], dp[i-1][j-c]+a)
print(bisect_left(dp[-1], m))
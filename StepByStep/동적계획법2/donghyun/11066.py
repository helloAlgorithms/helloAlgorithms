import sys

input = sys.stdin.readline
for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	subsum = {-1: 0}
	for i in range(n):
		subsum[i] = subsum[i - 1] + l[i]
	dp = [[0] * n for _ in range(n)]
	for x in range(1, n):
		for i in range(n - x):
			j = i + x
			dp[i][j] = float("inf")
			for k in range(i, j):
				dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + subsum[j] - subsum[i - 1])
	print(dp[0][-1])
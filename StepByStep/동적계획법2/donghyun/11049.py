import sys

input = sys.stdin.readline
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
for x in range(1, n):
	for i in range(n - x):
		j = i + x
		dp[i][j] = float("inf")
		for k in range(i, j):
			dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + l[i][0] * l[k][1] * l[j][1])
print(dp[0][-1])
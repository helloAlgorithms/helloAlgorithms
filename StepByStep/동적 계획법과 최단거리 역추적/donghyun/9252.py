import sys

input = sys.stdin.readline
a = ' ' + input().strip()
b = ' ' + input().strip()
dp = [[""] * len(b) for _ in range(len(a))]
for i in range(1, len(a)):
	for j in range(1, len(b)):
		if a[i] == b[j]:
			dp[i][j] = dp[i - 1][j - 1] + a[i]
		else:
			dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
print(len(dp[-1][-1]))
print(dp[-1][-1])
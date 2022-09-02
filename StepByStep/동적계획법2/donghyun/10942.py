import sys

input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]
for x in range(n):
	for i in range(n - x):
		j = i + x
		if i == j:
			dp[i][j] = 1
		elif l[i] == l[j]:
			if j - i == 1 or dp[i + 1][j - 1]:
				dp[i][j] = 1
for _ in range(int(input())):
	s, e = map(int, input().split())
	print(dp[s - 1][e - 1])
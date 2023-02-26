t = int(input())
dp = [0,1, 2, 4] + [0] * 8
for _ in range(t):
	n = int(input())
	def d(i):
		if dp[i] != 0:
			return dp[i]
		dp[i] = d(i - 1) + d(i - 2) + d(i - 3)
		return dp[i]
	print(d(n))

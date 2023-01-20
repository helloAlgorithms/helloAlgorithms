t = int(input())
dp = [[None for c in range(15)] for r in range(15)]
for _ in range(1, 15):
	dp[0][_] = _
def mem(r, c):
	if r == 0: return c
	if c == 0: return 0
	if dp[r][c] != None: return dp[r][c]
	dp[r][c] = mem(r, c - 1) + mem(r - 1, c)
	return dp[r][c]
for _ in range(t):
	print(mem(int(input()), int(input())))

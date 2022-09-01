import sys

input = sys.stdin.readline
m, n = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(m)]
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
def dfs(x, y):
	if x == m - 1 and y == n - 1:
		return 1
	if dfs.dp[x][y] != -1:
		return dfs.dp[x][y]
	routes = 0
	for i in range(4):
		mx, my = x + dx[i], y + dy[i]
		if 0 <= mx < m and 0 <= my < n and l[mx][my] < l[x][y]:
			routes += dfs(mx, my)
	dfs.dp[x][y] = routes
	return dfs.dp[x][y]
dfs.dp = [[-1] * n for _ in range(m)]
print(dfs(0, 0))
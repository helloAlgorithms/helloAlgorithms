import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, r, q = map(int, input().split())
tree = [[] for _ in range(n + 1)]
dp = [0] * (n + 1)
for _ in range(n - 1):
	u, v = map(int, input().split())
	tree[u].append(v)
	tree[v].append(u)
def dfs(visit, parent):
	dp[visit] = 1
	for route in tree[visit]:
		if route != parent:
			dfs(route, visit)
			dp[visit] += dp[route]
dfs(r, 0)
for _ in range(q):
	print(dp[int(input())])
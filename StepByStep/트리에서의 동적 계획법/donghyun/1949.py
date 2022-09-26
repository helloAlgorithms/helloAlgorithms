import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))
tree = [[] for _ in range(n + 1)]
dp = [[0, 0] for _ in range(n + 1)]
for _ in range(n - 1):
	u, v = map(int, input().split())
	tree[u].append(v)
	tree[v].append(u)
def dfs(visit, parent):
	dp[visit][1] = p[visit-1]
	for route in tree[visit]:
		if route != parent:
			dfs(route, visit)
			dp[visit][0] += max(dp[route][0], dp[route][1])
			dp[visit][1] += dp[route][0]
dfs(1, 0)
print(max(dp[1][0], dp[1][1]))
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input())
tree = defaultdict(list)
for _ in range(n - 1):
	u, v = map(int, input().split())
	tree[u].append(v)
	tree[v].append(u)
dp = defaultdict(lambda: [0, 0])

def dfs(x, parent):
	dp[x][0] = 0
	dp[x][1] = 1
	for i in tree[x]:
		if i != parent:
			dfs(i, x)
			dp[x][0] += dp[i][1]
			dp[x][1] += min(dp[i][0], dp[i][1])

dfs(1, 0)
print(min(dp[1][0], dp[1][1]))
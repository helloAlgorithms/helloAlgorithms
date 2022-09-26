import sys

input = sys.stdin.readline
n = int(input())
w = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
dp = [[0, 0] for _ in range(n + 1)]
trace = [[[], []] for _ in range(n + 1)]
for _ in range(n - 1):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)
def dfs(x, parent):
	dp[x][0] = 0
	dp[x][1] = w[x]
	trace[x][1].append(x)
	for i in graph[x]:
		if i != parent:
			dfs(i, x)
			dp[x][0] += max(dp[i][0], dp[i][1])
			trace[x][0] += trace[i][1] if dp[i][1] > dp[i][0] else trace[i][0]
			dp[x][1] += dp[i][0]
			trace[x][1] += trace[i][0]
dfs(1, 0)
print(dp[1][dp[1][1] > dp[1][0]])
print(*sorted(trace[1][dp[1][1] > dp[1][0]]))
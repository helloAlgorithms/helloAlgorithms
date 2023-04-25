n, m = map(int, input().split())
import sys
sys.setrecursionlimit(10**6)
graph = {}
visited = [False] * (n + 1)
cnt = 0
for _ in range(m):
	f, t = map(int, input().split())
	tmp = graph.keys()
	if f in tmp:
		graph[f].append(t)
		if t in tmp:
			graph[t].append(f)
		else:
			graph[t] = [f]
	else:
		graph[f] = [t]
		if t in tmp:
			graph[t].append(f)
		else:
			graph[t] = [f]
keys = list(graph.keys())
def dfs(v):
    if visited[v]:return
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)

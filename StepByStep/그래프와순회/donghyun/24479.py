import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
node, edge, start = map(int, input().split())
graph = [[] for _ in range(node + 1)]
for i in range(edge):
	f, t = map(int, input().split())
	graph[f].append(t)
	graph[t].append(f)
graph = [sorted(routes) for routes in graph]

def dfs(visit):
	dfs.visited.add(visit)
	dfs.to_print[visit - 1] = dfs.order
	dfs.order += 1
	for route in graph[visit]:
		if route not in dfs.visited:
			dfs(route)
dfs.visited = set()
dfs.to_print = [0] * node
dfs.order = 1
dfs(start)
print(*dfs.to_print)
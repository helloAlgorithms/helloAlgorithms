import sys
from collections import deque

input = sys.stdin.readline
node, edge, start = map(int, input().split())
graph = [[] for _ in range(node + 1)]
for _ in range(edge):
	f, t = map(int, input().split())
	graph[f].append(t)
	graph[t].append(f)
graph = [sorted(routes) for routes in graph]

def dfs(visit):
	for route in graph[visit]:
		if route not in dfs.visited:
			dfs.visited.add(route)
			dfs.to_print.append(route)
			dfs(route)
dfs.visited = set([start])
dfs.to_print = [start]

def bfs():
	q = deque([start])
	while q:
		visit = q.popleft()
		for route in graph[visit]:
			if route not in bfs.visited:
				bfs.visited.add(route)
				bfs.to_print.append(route)
				q.append(route)
bfs.visited = set([start])
bfs.to_print = [start]

dfs(start)
bfs()
print(*dfs.to_print)
print(*bfs.to_print)
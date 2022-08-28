import sys
from collections import deque

input = sys.stdin.readline
node, edge, start = map(int, input().split())
graph = [[] for _ in range(node + 1)]
for i in range(edge):
	f, t = map(int, input().split())
	graph[f].append(t)
	graph[t].append(f)
graph = [sorted(routes, reverse=True) for routes in graph]

def bfs():
	bfs.visited.add(start)
	q = deque([start])
	while q:
		visit = q.popleft()
		bfs.to_print[visit - 1] = bfs.order
		bfs.order += 1
		for route in graph[visit]:
			if route not in bfs.visited:
				bfs.visited.add(route)
				q.append(route)
bfs.visited = set()
bfs.to_print = [0] * node
bfs.order = 1
bfs()
print(*bfs.to_print)
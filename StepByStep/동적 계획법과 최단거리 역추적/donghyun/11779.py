import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for i in range(m):
	u, v, w = map(int, input().split())
	graph[u].append([w, v])
start, goal = map(int, input().split())
def dijkstra(start):
	q = [(0, start)]
	trace = {}
	start_end = [float("inf")] * (n + 1)
	start_end[start] = 0
	while q:
		start_mid, visit = heappop(q)
		if start_mid > start_end[visit]:
			continue
		for mid_end, route in graph[visit]:
			if (distance:=start_mid + mid_end) < start_end[route]:
				heappush(q, (distance, route))
				start_end[route] = distance
				trace[route] = visit
	return start_end, trace
dj, tr = dijkstra(start)
print(dj[goal])
path = [goal]
while start != goal:
	path.append(goal:=tr[goal])
print(len(path))
print(*path[::-1])
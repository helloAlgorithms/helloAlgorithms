import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]
for i in range(E):
	u, v, w = map(int, input().split())
	graph[u].append([w, v])
def dijkstra(start, first=1):
	q = [[0, start]]
	start_end = [float("inf")] * (V + first)
	start_end[start] = 0
	while q:
		start_mid, visit = heapq.heappop(q)
		for mid_end, route in graph[visit]:
			if (distance:=start_mid + mid_end) < start_end[route]:
				heapq.heappush(q, [distance, route])
				start_end[route] = distance
	return start_end
for i, d in enumerate(dijkstra(start)):
	if i:
		print(str(d).upper())
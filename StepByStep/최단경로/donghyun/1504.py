import sys
import heapq

input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(E):
	u, v, w = map(int, input().split())
	graph[u].append([w, v])
	graph[v].append([w, u])
u, v = map(int, input().split())
def dijkstra(start, f=1):
	q = [[0, start]]
	start_end = [float("inf")] * (N + f)
	start_end[start] = 0
	while q:
		start_mid, visit = heapq.heappop(q)
		for mid_end, route in graph[visit]:
			if (distance:=start_mid + mid_end) < start_end[route]:
				heapq.heappush(q, [distance, route])
				start_end[route] = distance
	return start_end
d1, du, dv = dijkstra(1), dijkstra(u), dijkstra(v)
dist = min(d1[u] + du[v] + dv[N], d1[v] + dv[u] + du[N])
print(-1 if dist == float("inf") else dist)	
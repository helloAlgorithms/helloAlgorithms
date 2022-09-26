import sys
import heapq

input = sys.stdin.readline
for _ in range(int(input())):
	n, m, t = map(int, input().split())
	s, g, h = map(int, input().split())
	graph = {i: {} for i in range(n + 1)}
	for _ in range(m):
		a, b, d = map(int, input().split())
		graph[a][b] = d
		graph[b][a] = d
	def dijkstra(start, f=1, n=n, g=graph):
		q = [[0, start]]
		start_end = [float("inf")] * (n + f)
		start_end[start] = 0
		while q:
			start_mid, visit = heapq.heappop(q)
			for route, mid_end in g[visit].items():
				if (distance:=start_mid + mid_end) < start_end[route]:
					heapq.heappush(q, [distance, route])
					start_end[route] = distance
		return start_end
	ds, dg, dh = dijkstra(s), dijkstra(g), dijkstra(h)
	ans = []
	for _ in range(t):
		goal = int(input())
		dist = min(ds[g] + graph[g][h] + dh[goal], ds[h] + graph[g][h] + dg[goal])
		if dist == ds[goal] and dist != float("inf"):
			ans.append(goal)
	print(*sorted(ans))
import sys
import heapq

input = sys.stdin.readline
N, K = map(int, input().split())
def graph(x):
	route = []
	if x - 1 >= 0: route.append((1, x - 1))
	if x + 1 <= 100000: route.append((1, x + 1))
	if 2 * x <= 100000: route.append((0, 2 * x))
	return route
def dijkstra(start, first=0, n=100001, g=graph):
	q = [[0, start]]
	start_end = [float("inf")] * (n + first)
	start_end[start] = 0
	while q:
		start_mid, visit = heapq.heappop(q)
		for mid_end, route in g(visit):
			if (distance:=start_mid + mid_end) < start_end[route]:
				heapq.heappush(q, [distance, route])
				start_end[route] = distance
	return start_end
print(dijkstra(N)[K])
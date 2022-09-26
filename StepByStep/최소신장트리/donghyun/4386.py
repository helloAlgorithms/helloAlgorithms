import sys
import heapq
from collections import deque

input = sys.stdin.readline
n = int(input())
routes = [tuple(map(float, input().split())) for _ in range(n)]
q = deque([routes[0]])
visited = set([routes[0]])
edges = []
dist = lambda a, b : ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
w = c = 0
while q and c < n - 1:
	visit = q.popleft()
	for route in routes:
		if route not in visited:
			heapq.heappush(edges, (dist(visit, route), route))
	while edge:=heapq.heappop(edges):
		if edge[-1] not in visited:
			break
	q.append(edge[-1])
	visited.add(edge[-1])
	w += edge[0]
	c += 1
print(round(w, 2))
import sys
import heapq
from math import dist

input = sys.stdin.readline
n, m = map(int, input().split())
vertexs = {i: tuple(map(int, input().split())) for i in range(1, n + 1)}
uf = list(range(n + 1))

def find(x):
	if uf[x] == x:
		return x
	uf[x] = find(uf[x])
	return uf[x]

def union(x, y):
	x, y = find(x), find(y)
	uf[min(x, y)] = max(x, y)

count = 0
edges = []
for _ in range(m):
	a, b = map(int, input().split())
	heapq.heappush(edges, (dist(vertexs[a], vertexs[b]), a, b))
while edges:
	_, a, b = heapq.heappop(edges)
	if find(a) != find(b):
		union(a, b)
		count += 1
edges = []
for i in vertexs:
	for j in vertexs:
		if i != j:
			heapq.heappush(edges, (dist(vertexs[i], vertexs[j]), i, j))
weight = 0
while count < n - 1:
	d, a, b = heapq.heappop(edges)
	if find(a) != find(b):
		union(a, b)
		weight += d
		count += 1
print(f"{weight:.2f}")
import sys
import heapq

input = sys.stdin.readline
v, e = map(int, input().split())
w = n = 0
edges = []
uf = list(range(v + 1))
for _ in range(e):
	a, b, c = map(int, input().split())
	heapq.heappush(edges, (c, a, b))

def find(x):
	if x == uf[x]:
		return x
	uf[x] = find(uf[x])
	return uf[x]

def union(x, y):
	x, y = find(x), find(y)
	if x != y:
		uf[min(x, y)] = max(x, y)

while n < v - 1:
	c, a, b = heapq.heappop(edges)
	if find(a) != find(b):
		union(a, b)
		w += c
		n += 1
print(w)
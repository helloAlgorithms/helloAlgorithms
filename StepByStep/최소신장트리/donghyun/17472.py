import sys
from collections import deque
from heapq import heappush, heappop
from copy import deepcopy

input = sys.stdin.readline
n, m = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]
back_up = deepcopy(country)

islands = []
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
def bfs(x, y):
	q = deque([(x, y)])
	visited = set([(x, y)])
	country[x][y] = 0
	while q:
		x, y = q.popleft()
		for i in range(4):
			mx, my = x + dx[i], y + dy[i]
			if 0 <= mx < n and 0 <= my < m and country[mx][my]:
				route = (mx, my)
				if route not in visited:
					q.append(route)
					visited.add(route)
					country[mx][my] = 0
	islands.append(visited)
for i in range(n):
	for j in range(m):
		if country[i][j]:
			bfs(i, j)
country = back_up

bridges = []
for start, island in enumerate(islands):
	for coast in island:
		for i in range(4):
			x, y = coast
			mx, my = x + dx[i], y + dy[i]
			length = 0
			while 0 <= mx < n and 0 <= my < m and not country[mx][my]:
				mx, my = mx + dx[i], my + dy[i]
				length += 1
			if length > 1 and 0 <= mx < n and 0 <= my < m:
				for end, dest in enumerate(islands):
					if start != end and (mx, my) in dest:
						heappush(bridges, (length, start, end))

uf = list(range(len(islands)))
def find(x):
	if uf[x] == x:
		return x
	uf[x] = find(uf[x])
	return uf[x]
def union(x, y):
	x, y = find(x), find(y)
	uf[min(x, y)] = max(x, y)

weight = count = 0
while count < len(islands) - 1 and bridges:
	w, a, b = heappop(bridges)
	if find(a) != find(b):
		union(a, b)
		weight += w
		count += 1

for i in uf:
	if find(i) != find(0):
		weight = -1
print(weight or -1)
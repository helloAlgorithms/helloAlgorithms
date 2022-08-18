import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

def bfs(i, j):
	dx, dy = [1, -1, 0, 0], [0, 0 , 1, -1]
	q = deque([(i, j)])
	graph[i][j] = 0
	house = 1
	while q:
		visit = q.popleft()
		x, y = visit
		for i in range(4):
			mx, my = x + dx[i], y + dy[i]
			if 0 <= mx < n and 0 <= my < n and graph[mx][my]:
				q.append((mx, my))
				graph[mx][my] = 0
				house += 1
	return house

cluster = 0
houses = []
for i in range(n):
	for j in range(n):
		if graph[i][j]:
			houses.append(bfs(i, j))
			cluster += 1
print(cluster)
print(*sorted(houses), sep="\n")
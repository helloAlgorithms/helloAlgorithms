import sys
from collections import deque

input = sys.stdin.readline
c = int(input())
for _ in range(c):
	m, n, k = map(int, input().split())
	graph = [[0] * n for _ in range(m)]
	for _ in range(k):
		i, j = map(int, input().split())
		graph[i][j] = 1

	def bfs(i, j):
		dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
		q = deque([(i, j)])
		graph[i][j] = 0
		while q:
			visit = q.popleft()
			x, y = visit
			for i in range(4):
				mx, my = x + dx[i], y + dy[i]
				if 0 <= mx < m and 0 <= my < n and graph[mx][my]:
					graph[mx][my] = 0
					q.append((mx, my))

	worm = 0
	for i in range(m):
		for j in range(n):
			if graph[i][j]:
				bfs(i, j)
				worm += 1
	print(worm)
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
q = deque([(0, 0, 1)])
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
while q:
	x, y, d = q.popleft()
	if x == n - 1 and y == m - 1:
		print(d)
	for i in range(4):
		mx, my = x + dx[i], y + dy[i]
		if 0 <= mx < n and 0 <= my < m and graph[mx][my]:
			graph[mx][my] = 0
			q.append((mx, my, d + 1))

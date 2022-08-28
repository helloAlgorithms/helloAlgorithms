import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
tomato = set([(i, j) for i in range(n) for j in range(m) if graph[i][j]==1])
day = -1
q = deque(tomato)
q_next = deque()
while q:
	x, y = q.popleft()
	dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
	for i in range(4):
		mx, my = x + dx[i], y + dy[i]
		if 0 <= mx < n and 0 <= my < m and graph[mx][my] == 0:
			graph[mx][my] = 1
			q_next.append((mx, my))
	if not q:
		q, q_next, day = q_next, deque(), day + 1
if [1 for i in range(n) for j in range(m) if graph[i][j] == 0]:
	print(-1)
else:
	print(day)
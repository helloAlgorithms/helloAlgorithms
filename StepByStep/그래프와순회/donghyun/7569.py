import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
tomato = set([(i, j, k) for i in range(n) for j in range(m) for k in range(h) if graph[k][i][j]==1])
day = -1
q = deque(tomato)
q_next = deque()
while q:
	x, y, z = q.popleft()
	dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
	for i in range(6):
		mx, my, mz = x + dx[i], y + dy[i], z + dz[i]
		if 0 <= mx < n and 0 <= my < m and 0 <= mz < h and graph[mz][mx][my]== 0:
			graph[mz][mx][my] = 1
			q_next.append((mx, my, mz))
	if not q:
		q, q_next, day = q_next, deque(), day + 1
if [1 for i in range(n) for j in range(m) for k in range(h) if graph[k][i][j] == 0]:
	print(-1)
else:
	print(day)
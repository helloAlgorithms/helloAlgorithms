import sys
from collections import deque

input = sys.stdin.readline
c = int(input())
for _ in range(c):
	I = int(input())
	fx, fy = map(int, input().split())
	tx, ty = map(int, input().split())
	graph = [[1] * I for _ in range(I)]
	graph[fx][fy] = t = 0
	q = deque([(fx, fy, t)])
	dx, dy = [-1, -1, -2, -2, 1, 1, 2, 2], [2, -2, 1, -1, 2, -2, 1, -1]
	while fx != tx or fy != ty:
		fx, fy, t = q.popleft()
		for i in range(8):
			x, y = fx + dx[i], fy + dy[i]
			if 0 <= x < I and 0 <= y < I and graph[x][y]:
				graph[x][y] = 0
				q.append((x, y, t + 1))
	print(t)
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
q = deque([(0, 0, 0)])
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
visited = [[[-1, -1] for _ in range(m)] for _ in range(n)]
visited[0][0] = [1, 1]
while q:
    x, y, z = q.popleft()
    step = visited[x][y][z]
    for i in range(4):
        mx, my = x + dx[i], y + dy[i]
        if 0 <= mx < n and 0 <= my < m and visited[mx][my][z] == -1:
            if graph[mx][my] and z == 0:
                q.append((mx, my, 1))
                visited[mx][my][1] = step + 1
            elif graph[mx][my] == 0:
                q.append((mx, my, z))
                visited[mx][my][z] = step + 1
print(max(v) if -1 in (v:=visited[-1][-1]) else min(v))
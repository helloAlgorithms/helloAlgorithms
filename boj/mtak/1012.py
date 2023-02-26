import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for __ in range(n)]
    cnt = 0
    def bfs(y, x):
        queue = list()
        graph[y][x] = 0
        queue.append((y, x))
        while queue:
            y, x = queue.pop(0)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    queue.append((ny, nx))

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for r in range(n):
        for c in range(m):
            if graph[r][c] == 1:
                bfs(r, c)
                cnt += 1
    print(cnt)
    
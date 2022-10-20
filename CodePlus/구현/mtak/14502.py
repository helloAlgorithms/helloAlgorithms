from collections import deque
import graphlib
import sys
from collections import deque
import copy

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().strip().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
def bfs():
    queue = deque()
    tg = copy.deepcopy(graph)
    for r in range(n):
        for c in range(m):
            if tg[r][c] == 2:
                queue.append((r, c))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tg[nx][ny] == 0:
                tg[nx][ny] = 2
                queue.append((nx, ny))
    global ans
    cnt = 0
    for i in range(n):
        cnt += tg[i].count(0)
    ans = max(ans, cnt)

def setWall(cnt):
    if cnt == 3:
        bfs()
        return
    for r in range(n):
        for c in range(m):
            if graph[r][c] == 0:
                graph[r][c] = 1
                setWall(cnt + 1)
                graph[r][c] = 0
setWall(0)
print(ans)

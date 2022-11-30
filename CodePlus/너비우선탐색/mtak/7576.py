import sys
input = sys.stdin.readline
m , n = map(int, input().split())
t = [list(map(int, input().strip().split())) for _ in range(n)]
cnt = 0
dx = [0,0,1, -1]
dy = [1, -1, 0, 0]
q = []
for y in range(n):
    for x in range(m):
        if t[y][x] == 1:
            q.append((y, x))
def bfs():
    while q:
        y, x = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny <0 or ny >= n:
                continue
            if t[ny][nx] == 0:
                t[ny][nx] = t[y][x] + 1
                q.append((ny, nx))
bfs()
for r in t:
    for c in r:
        if c == 0:
            exit()
    cnt = max(cnt, max(r))
print(cnt - 1)

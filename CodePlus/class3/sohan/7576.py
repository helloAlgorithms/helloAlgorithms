from collections import deque

N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(M)]
v = [[0 for i in range(N)] for j in range(M)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def find(m, val):
    s = deque()
    for i in range(M):
        for j in range(N):
            if m[i][j] == val:
                s.append([i, j])
    return s

q = find(m, 1)
a = 0

while len(q) != 0:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < M and nx >= 0 and ny < N and ny >= 0:
            if m[nx][ny] == 0 and v[nx][ny] == 0:
                m[nx][ny] = 1
                v[nx][ny] = v[x][y] + 1
                q.append([nx, ny])
                a = v[nx][ny]
z = find(m, 0)
if len(z) != 0:
    print(-1)
else:
    print(a)

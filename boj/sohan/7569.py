from collections import deque

M, N, H = map(int, input().split(' '))
boxes = []

dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for j in range(H):
    tmp = [input().split(' ') for i in range(N)]
    boxes.append(tmp)

def find(c):
    l = []
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if boxes[i][j][k] == c:
                    l.append((i, j, k))
    return l

if len(find('0')) == 0:
    print('0')
    exit(0)

t = 0

q = deque()
ls = find('1')
for l in ls:
    q.append((l, t))

while q:
    coor, t = q.popleft()
    z, x, y = coor
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
            if boxes[nz][nx][ny] == '0':
                boxes[nz][nx][ny] = '1'
                q.append(((nz, nx, ny), t + 1))

if len(find('0')) != 0:
    print("-1")
else:
    print(t)
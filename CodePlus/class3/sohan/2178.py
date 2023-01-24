N, M = map(int, input().split())
maze = [list(map(str, input())) for _ in range(N)]
v = [[0 for i in range(M)] for j in range(N)]
q = []
q.append([0,0])
v[0][0] = 1

while len(q) != 0:
    x = q.pop(0)
    if x == [N - 1, M - 1]:
        break
    
    nx = x[0] + 1
    ny = x[1] + 1
    nd = v[x[0]][x[1]] + 1

    if nx < N and maze[nx][x[1]] != '0' and v[nx][x[1]] == 0:
        v[nx][x[1]] = nd
        q.append([nx, x[1]])

    if ny < M and maze[x[0]][ny] != '0' and v[x[0]][ny] == 0:
        v[x[0]][ny] = nd
        q.append([x[0], ny])
    
    if nx - 2 >= 0 and maze[nx - 2][x[1]] != '0' and v[nx - 2][x[1]] == 0:
        v[nx -2][x[1]] = nd
        q.append([nx - 2, x[1]])

    if ny - 2 >= 0 and maze[x[0]][ny - 2] != '0' and v[x[0]][ny - 2] == 0:
        v[x[0]][ny - 2] = nd
        q.append([x[0], ny - 2])

print(v[N - 1][M - 1])

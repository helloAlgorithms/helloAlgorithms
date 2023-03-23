from collections import deque

N = int(input())
space = [list(map(int, input().split(' '))) for _ in range(N)]
dy = [0, -1, 1, 0]
dx = [-1, 0, 0, 1]

t = 0
size = 2
count = 0

def find():
	for i in range(N):
		for j in range(N):
			if space[i][j] == 9:
				space[i][j] = 0
				return [i, j]

def bfs(a, b, t):
	global size

	visited = [[0 for i in range(N)] for j in range(N)]
	visited[a][b] = 1
	q = deque()
	catch = []
	q.append([a, b, t])

	while q:
		x, y, t = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
				if space[nx][ny] <= size:
					visited[nx][ny] = 1
					q.append([nx, ny, t + 1])
					if 0 < space[nx][ny] < size:
						catch.append((t + 1, nx, ny))
	
	return sorted(catch, key=lambda x : (-x[0], -x[1], -x[2]))

cur_x, cur_y = find()
space[cur_x][cur_y] = 0

while True:
	fishes = bfs(cur_x, cur_y, t)
	if len(fishes) == 0:
		break
	t, cur_x, cur_y = fishes.pop()
	space[cur_x][cur_y] = 0
	count += 1
	if count == size:
		size += 1
		count = 0
	
print(t)
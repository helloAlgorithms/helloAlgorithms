from collections import deque

N = int(input())
pic = [list(map(str, input())) for _ in range(N)]
visited = [[0 for i in range(N)] for j in range(N)]

def bfs(i, j, color):
	q = deque()
	q.append([i, j])
	
	dx = [0, 1, 0, -1]
	dy = [1, 0, -1, 0]

	while q:
		x, y = q.popleft()

		for k in range(4):
			nx = x + dx[k]
			ny = y + dy[k]
			if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and pic[nx][ny] == color:
				visited[nx][ny] = 1
				q.append([nx, ny])

area_count = 0
for i in range(N):
	for j in range(N):
		if visited[i][j] == 0:
			bfs(i, j, pic[i][j])
			area_count += 1

print(area_count, end=' ')

for i in range(N):
	for j in range(N):
		if pic[i][j] == 'G':
			pic[i][j] = 'R'

visited = [[0 for i in range(N)] for j in range(N)]
area_count = 0

for i in range(N):
	for j in range(N):
		if visited[i][j] == 0:
			bfs(i, j, pic[i][j])
			area_count += 1

print(area_count)
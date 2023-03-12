N, M = map(int, input().split(' '))

m = [list(map(int, input().split(' '))) for _ in range(N)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
visited = [[0 for i in range(M)] for j in range(N)]
ans = 0
max_val = max(map(max, m))

def dfs(x, y, depth, sum):
	global ans
	if sum + max_val * (4 - depth) <= ans:
		return
	if depth == 4:
		ans = max(ans, sum)
		return
	
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
			if depth == 2:
				visited[nx][ny] = 1
				dfs(x, y, depth + 1, sum + m[nx][ny])
				visited[nx][ny] = 0
			
			visited[nx][ny] = 1
			dfs(nx, ny, depth + 1, sum + m[nx][ny])
			visited[nx][ny] = 0

for i in range(N):
	for j in range(M):
		visited[i][j] = 1
		dfs(i, j, 1, m[i][j])
		visited[i][j] = 0

print(ans)
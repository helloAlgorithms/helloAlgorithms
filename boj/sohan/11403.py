N = int(input())
adj = [list(map(int, input().split(' '))) for _ in range(N)]

for k in range(N):
	for i in range(N):
		for j in range(N):
			if adj[i][k] == 1 and adj[k][j] == 1:
				adj[i][j] = 1

for _ in adj:
	print(*_)
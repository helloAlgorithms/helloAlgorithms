import sys
input = sys.stdin.readline
n = int(input())
_map = []
for _ in range(n):
	_map.append(list(input().strip()))
visit = []

def bfs(x, y):
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	queue = list()
	familyNum = 1
	_map[x][y] = '0'
	queue.append((x, y))
	while queue:
		x, y = queue.pop(0)
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or nx >= n or ny < 0 or ny >= n:
				continue
			if _map[nx][ny] == '1':
				familyNum += 1
				_map[nx][ny] = '0'
				queue.append((nx, ny))
	return familyNum

for r in range(n):
	for c in range(n):
		if _map[r][c] == '1':
			visit.append(bfs(r, c))
visit.sort()
print(len(visit))
for p in visit:
	print(p)

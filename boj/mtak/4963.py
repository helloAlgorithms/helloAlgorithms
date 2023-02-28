while True:
	w, h = map(int, input().split())
	if w == 0 and h == 0:
		break
	_map = []
	for _ in range(h):
		_map.append(list(input().strip().split()))
	dx = [-1, 1, 0, 0, -1, 1, -1, 1]
	dy = [0, 0, -1, 1, -1, 1, 1, -1]
	def bfs(x, y):
		queue = list()
		_map[y][x] = '0'
		queue.append((x, y))
		while queue:
			x, y = queue.pop(0)
			for i in range(8):
				nx = x + dx[i]
				ny = y + dy[i]
				if nx < 0 or nx >= w or ny < 0 or ny >= h:
					continue
				if _map[ny][nx] == '1':
					_map[ny][nx] = '0'
					queue.append((nx, ny))
		return 1
	cnt = 0
	for hh in range(h):
		for ww in range(w):
			if _map[hh][ww] == '1':
				cnt += bfs(ww, hh)
	print(cnt)


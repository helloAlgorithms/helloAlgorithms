import sys
input = sys.stdin.readline
cnt = int(input())
pairCnt = int(input())
_map = {}
for _ in range(1, cnt + 1):
	_map[_] = []
for _ in range(pairCnt):
	x, y = map(int, input().split())
	_map.get(x).append(y)
	_map.get(y).append(x)
def bfs(v):
	visit = list()
	queue = list()
	queue.append(v)
	while queue:
		node = queue.pop(0)
		if node not in visit:
			visit.append(node)
			queue.extend(_map[node])
	return len(visit) - 1

print(bfs(1))

import sys
from collections import deque

input = sys.stdin.readline
def bfs(node):
	q = deque([node])
	tree = True
	while q:
		visit = q.popleft()
		if visit in bfs.visited:
			tree = False
		bfs.visited.add(visit)
		for route in bfs.tree[visit]:
			if route not in bfs.visited:
				q.append(route)
	return tree
case = 0
while True:
	n, m = map(int, input().split())
	if not n and not m:
		break
	bfs.tree = {i: [] for i in range(1, n + 1)}
	bfs.visited = set()
	for _ in range(m):
		v, w = map(int, input().split())
		bfs.tree[v].append(w)
		bfs.tree[w].append(v)
	count = 0
	case += 1
	for i in range(1, n + 1):
		if i not in bfs.visited:
			count += bfs(i)
	if count == 0:
		print(f"Case {case}: No trees.")
	elif count == 1:
		print(f"Case {case}: There is one tree.")
	else:
		print(f"Case {case}: A forest of {count} trees.")
	
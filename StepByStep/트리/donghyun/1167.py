import sys

input = sys.stdin.readline
v = int(input())
tree = {i : {} for i in range(1, v + 1)}
for _ in range(v):
	gen = map(int, input().split())
	node1 = next(gen)
	while (node2 := next(gen)) != -1:
		tree[node1][node2] = next(gen)
def dfs(visit, total):
	leaf = True
	dfs.visited.add(visit)
	for route, dist in tree[visit].items():
		if dist and route not in dfs.visited:
			dfs(route, total + dist)
			leaf = False
	if leaf:
		if total > dfs.max:
			dfs.max = total
			dfs.farthest = visit
dfs.visited = set()
dfs.max = 0
dfs(1, 0)
dfs.visited = set()
dfs.max = 0
dfs(dfs.farthest, 0)
print(dfs.max)
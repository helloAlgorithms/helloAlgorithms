import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
v = int(input())
tree = {i : {} for i in range(1, v + 1)}
for _ in range(v - 1):
	parent, child, dist = map(int, input().split())
	tree[parent][child] = dist
	tree[child][parent] = dist
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
dfs.max = -1
dfs(1, 0)
dfs.visited = set()
dfs.max = -1
dfs(dfs.farthest, 0)
print(dfs.max)
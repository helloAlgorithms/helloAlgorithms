import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
	a, b = map(int, input().split())
	tree[a].append(b)
	tree[b].append(a)
q = deque([1])
visited = {1: 0}
while q:
	visit = q.popleft()
	for route in tree[visit]:
		if route not in visited:
			q.append(route)
			visited[route] = visit
for i in range(2, n + 1):
	print(visited[i])
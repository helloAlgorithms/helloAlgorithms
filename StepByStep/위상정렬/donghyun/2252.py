import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
for _ in range(m):
	u, v = map(int, input().split())
	graph[u].append(v)
	indegree[v] += 1
q = deque((i for i in range(1, n + 1) if indegree[i] == 0))
answer = []
while q:
	visit = q.popleft()
	answer.append(visit)
	for route in graph[visit]:
		indegree[route] -= 1
		if indegree[route] == 0:
			q.append(route)
print(*answer)
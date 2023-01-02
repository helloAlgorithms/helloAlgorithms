import sys
from heapq import heappush, heappop

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
for _ in range(m):
	u, v = map(int, input().split())
	graph[u].append(v)
	indegree[v] += 1
q = []
for i in range(1, n + 1):
	if indegree[i] == 0:
		heappush(q, i)
answer = []
while q:
	visit = heappop(q)
	answer.append(visit)
	for route in graph[visit]:
		indegree[route] -= 1
		if indegree[route] == 0:
			heappush(q, route)
print(*answer)
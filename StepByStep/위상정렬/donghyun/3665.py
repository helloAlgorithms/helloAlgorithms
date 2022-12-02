import sys
from collections import deque

input = sys.stdin.readline
for _ in range(int(input())):
	n = int(input())
	graph = {}
	indegree = {}
	for i, j in enumerate(map(int, input().split())):
		for k in graph:
			graph[k].add(j)
		graph[j] = set()
		indegree[j] = i
	for _ in range(int(input())):
		u, v = map(int, input().split())
		if v in graph[u]:
			u, v = v, u
		graph[u].add(v)
		graph[v].discard(u)
		indegree[u] -= 1
		indegree[v] += 1
	q = deque((i for i in range(1, n + 1) if not indegree[i]))
	answer = []
	while q:
		visit = q.popleft()
		answer.append(visit)
		for route in graph[visit]:
			indegree[route] -= 1
			if indegree[route] == 0:
				q.append(route)
	if len(answer) == n:
		print(*answer)
	else:
		print("IMPOSSIBLE")
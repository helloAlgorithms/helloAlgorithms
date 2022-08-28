import sys
from collections import deque

input = sys.stdin.readline
case = int(input())
for _ in range(case):
	node, edge = map(int, input().split())
	group = [0] * (node + 1)
	graph = [[] for _ in range(node + 1)]
	for _ in range(edge):
		f, t = map(int, input().split())
		graph[f].append(t)
		graph[t].append(f)
	result = 1
	for i in range(1, node + 1):
		if not group[i] and result:
			q = deque()
			q.append(i)
			while q and result:
				visit = q.popleft()
				for route in graph[visit]:
					if not group[visit]:
						group[visit] = 1
					if not group[route]:
						group[route] = 3 - group[visit]
						q.append(route)
					if group[visit] == group[route]:
						result = 0
						break
	print("YES" if result else "NO")
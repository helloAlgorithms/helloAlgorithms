import sys
from collections import deque

input = sys.stdin.readline
for _ in range(int(input())):
	start, goal = map(int, input().split())
	q = deque([(start, "")])
	visit = start
	visited = set()
	while visit != goal:
		visit, trace = q.popleft()
		for i, route in enumerate((visit * 2 % 10000, visit - 1 if visit else 9999, \
			(visit % 1000) * 10 + visit // 1000, (visit % 10) * 1000 + visit // 10)):
			if route not in visited:
				visited.add(route)
				q.append((route, trace + "DSLR"[i]))
	print(trace)
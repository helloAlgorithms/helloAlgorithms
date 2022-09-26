import sys

input = sys.stdin.readline
n, m = map(int, input().split())
edges = []
for _ in range(m):
	a, b, c = map(int, input().split())
	edges.append((a, b, c))
start_to = {i: float("inf") for i in range(1, n + 1)}
def bellman_ford(start):
	start_to[start] = 0
	for i in range(1, n + 1):
		for j in range(m):
			a, b, c = edges[j]
			if start_to[a] != float("inf") and start_to[b] > start_to[a] + c:
				start_to[b] = start_to[a] + c
				if i == n:
					return True
	return False
cycle = bellman_ford(1)
if cycle:
	print(-1)
else:
	for i in range(2, n + 1):
		print(-1 if start_to[i] == float("inf") else start_to[i])
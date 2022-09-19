import sys

input = sys.stdin.readline
v, e = map(int, input().split())
graph = {i:{j: float("inf") for j in range(1, v + 1)} for i in range(1, v + 1)}
for _ in range(e):
	a, b, c = map(int, input().split())
	graph[a][b] = c
for k in range(1, v + 1):
	for i in range(1, v + 1):
		for j in range(1, v + 1):
			graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
cycle = min(graph[i][i] for i in range(1, v + 1))
print(-1 if cycle == float("inf") else cycle)
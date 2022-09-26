import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = {i :{j:float("inf") for j in range(1, n+1)} for i in range(1, n+1)}
for i in range(1, n + 1):
	graph[i][i] =0
for i in range(m):
	a, b, c = map(int, input().split())
	graph[a][b] = min(c, graph[a][b])
for k in range(1, n+1):
	for i in range(1, n+1):
		for j in range(1, n+1):
			graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
for i in range(1, n+1):
	print(*(0 if j == float("inf") else j for j in graph[i].values()), sep=" ")
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
from_to = [[float("inf")] * (n + 1) for _ in range(n + 1)]
trace = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
	from_to[i][i] = 0
for _ in range(m):
	a, b, c = map(int, input().split())
	if c < from_to[a][b]:
		from_to[a][b] = c
		trace[a][b] = [a, b]
def floyd_warshall():
	for k in range(1, n + 1):
		for i in range(1, n + 1):
			for j in range(1, n + 1):
				if (distance:=from_to[i][k] + from_to[k][j]) < from_to[i][j]:
					from_to[i][j] = distance
					trace[i][j] = trace[i][k] + trace[k][j][1:]
floyd_warshall()
for i in range(1, n + 1):
	print(*(cost if (cost:=from_to[i][j])!=float("inf") else 0 for j in range(1, n + 1)))
for i in range(1, n + 1):
	for j in range(1, n + 1):
		if from_to[i][j] == float("inf"):
			print(0)
		else:
			print(len(trace[i][j]), *trace[i][j])
import sys

input = sys.stdin.readline
n1, m1 = map(int, input().split())
mat1 = [list(map(int, input().split())) for _ in range(n1)]
n2, m2 = map(int, input().split())
mat2 = [list(map(int, input().split())) for _ in range(n2)]
res = [[0] * m2 for _ in range(n1)]
for i in range(n1):
	for j in range(m2):
		res[i][j] = sum([mat1[i][k] * mat2[k][j] for k in range(m1)])
[print(*i) for i in res]
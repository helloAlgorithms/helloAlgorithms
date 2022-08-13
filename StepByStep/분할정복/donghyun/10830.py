import sys

input = sys.stdin.readline
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

def matmul(m1, m2=None):
	ret = [[0] * n for _ in range(n)]
	if not m2:
		m2 = m1
	for i in range(n):
		for j in range(n):
			ret[i][j] = sum([m1[i][k] * m2[k][j] for k in range(n)]) % 1000
	return ret

def dq(mat, n):
	if n == 1:
		return mat
	if n == 2:
		return matmul(mat)
	if n % 2:
		return matmul(matmul(dq(mat, n//2)), mat)
	else:
		return matmul(dq(mat, n//2))

[print(*[j % 1000 for j in i]) for i in dq(mat, m)]
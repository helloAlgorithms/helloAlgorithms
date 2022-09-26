import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
def matmul(m1, m2=None):
	ret = [[0, 0], [0, 0]]
	if not m2:
		m2 = m1
	for i in range(2):
		for j in range(2):
			ret[i][j] = sum([m1[i][k] * m2[k][j] for k in range(2)]) % 1000000007
	return ret
def dq(mat, n):
	if n == 1:
		return mat
	if n == 2:
		return matmul(mat)
	if n % 2:
		return matmul(matmul(dq(mat, n//2)), mat)
	return matmul(dq(mat, n//2))
print(dq([[0, 1], [1, 1]], n)[0][1])
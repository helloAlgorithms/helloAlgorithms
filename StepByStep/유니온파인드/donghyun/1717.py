import sys

input = sys.stdin.readline
n, m = map(int,input().split())
uf = [i for i in range(n + 1)]

def find(x):
	if x == uf[x]:
		return x
	uf[x] = find(uf[x])
	return uf[x]

def union(x, y):
	x, y = find(x), find(y)
	uf[min(x, y)] = max(x, y)

for _ in range(m):
	op, a, b = map(int,input().split())
	if op == 0:
		union(a, b)
	elif op == 1:
		if find(a) == find(b):
			print('YES')
		else:
			print('NO')
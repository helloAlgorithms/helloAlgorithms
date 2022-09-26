import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
uf = list(range(n))

def find(x):
	if x == uf[x]:
		return x
	uf[x] = find(uf[x])
	return uf[x]

def union(x, y):
	x, y = find(x), find(y)
	if x != y:
		uf[min(x, y)] = max(x, y)

for i in range(1, m + 1):
	a, b = map(int, input().split())
	if find(a) == find(b):
		print(i)
		exit()
	union(a, b)
print(0)
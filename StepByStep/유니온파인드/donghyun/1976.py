import sys

input = sys.stdin.readline
n, m = int(input()), int(input())
uf = {i: i for i in range(1, n + 1)}

def find(x):
	if x == uf[x]:
		return x
	uf[x] = find(uf[x])
	return uf[x]

def union(x, y):
	x, y = find(x), find(y)
	uf[min(x, y)] = max(x, y)

for start in range(1, n + 1):
	connect = map(int, input().split())
	for to in range(1, n + 1):
		if next(connect):
			union(start, to)
sets = set(map(lambda x: find(int(x)), input().split()))
print(["NO", "YES"][len(sets) == 1])
import sys
from collections import defaultdict

input = sys.stdin.readline
for _ in range(int(input())):
	f = int(input())
	uf = defaultdict(str)
	count = defaultdict(int)

	def find(x):
		if not uf[x]:
			uf[x], count[x] = x, 1
		if x == uf[x]:
			return x
		uf[x] = find(uf[x])
		return uf[x]

	def union(x, y):
		x, y = find(x), find(y)
		if x != y:
			uf[min(x, y)] = max(x, y)
			count[max(x, y)] += count[min(x, y)]

	for _ in range(f):
		a, b = input().strip().split()
		union(a, b)
		print(count[find(a)])
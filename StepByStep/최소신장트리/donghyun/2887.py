import sys
from heapq import heappush, heappop

input = sys.stdin.readline
n = int(input())
xlst, ylst, zlst = [], [], []
for i in range(n):
	x, y, z = map(int, input().split())
	xlst.append((x, i))
	ylst.append((y, i))
	zlst.append((z, i))
xlst.sort()
ylst.sort()
zlst.sort()

uf = list(range(n))
def find(x):
	if uf[x] != x:
		uf[x] = find(uf[x])
	return uf[x]

def union(x, y):
	x, y = find(x), find(y)
	if x != y:
		uf[min(x, y)] = max(x, y)

edges = []
for lst in xlst, ylst, zlst:
	for i in range(1,n):
		w1, a = lst[i-1]
		w2, b = lst[i]
		heappush(edges, (abs(w2-w1), a, b))

weight = count = 0
while count < n - 1:
	w, a, b = heappop(edges)
	if find(a) != find(b):
		union(a,b)
		weight += w
		count += 1
print(weight)
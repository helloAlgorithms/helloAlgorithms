import heapq, sys

input = sys.stdin.readline
l, r = [10001], [10001]
for _ in range(int(input())):
	m = sorted([-heapq.heappop(l), int(input()), heapq.heappop(r)])
	print(m[1])
	heapq.heappush(l if (i:=len(l)!=len(r)) else r, (-1)**i*m[1])
	heapq.heappush(l, -m[0])
	heapq.heappush(r, m[2])
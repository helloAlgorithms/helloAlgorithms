import heapq, sys

input = sys.stdin.readline
l = []
for _ in range(int(input())):
	if n := int(input()):
		heapq.heappush(l, -n)
	else:
		print(-heapq.heappop(l) if len(l) else 0)
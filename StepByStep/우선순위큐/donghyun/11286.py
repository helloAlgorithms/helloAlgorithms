import heapq, sys

input = sys.stdin.readline
l = []
for _ in range(int(input())):
	if n := int(input()):
		heapq.heappush(l, [abs(n), n])
	else:
		print(heapq.heappop(l)[1] if len(l) else 0)
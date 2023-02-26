import sys
import heapq

N = int(input())
ops = [int(sys.stdin.readline()) for _ in range(N)]
h = []

for op in ops:
    if op > 0:
        heapq.heappush(h, -op)
    else:
        print("0" if len(h) == 0 else -heapq.heappop(h))

import sys
import heapq

N = int(input())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline().strip('\n'))
    if x == 0:
        n, sign = 0, 0
        if heap:
            n, sign = heapq.heappop(heap)
        print(n * sign)
    else:
        sign = 1
        if x < 0:
            x = -x
            sign = -1
        heapq.heappush(heap, (x, sign))

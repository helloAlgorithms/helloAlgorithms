import sys
import heapq

T = int(input())
for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    v = [False] * 1000001

    for key in range(k):
        o, n = sys.stdin.readline().strip().split(" ")
        if o == "I":
            heapq.heappush(min_heap, (int(n), key))
            heapq.heappush(max_heap, (-int(n), key))
            v[key] = True
        else:
            if n == "-1":
                while min_heap and not v[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    v[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            else:
                while max_heap and not v[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    v[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    while min_heap and not v[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not v[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
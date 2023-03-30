import sys
import heapq

N, M, X = map(int, input().split(' '))

adjs = [[] for _ in range(N)]

for i in range(M):
  start, end, T = map(int, sys.stdin.readline().strip().split(' '))
  adjs[start - 1].append((end - 1, T))

def distance(start):
  dist = [10e6 for _ in range(N)]
  heap = []
  dist[start] = 0
  heapq.heappush(heap, (0, start))
  while heap:
    cost, index = heapq.heappop(heap)
    for node in adjs[index]:
      if node[1] + cost < dist[node[0]]:
        dist[node[0]] = node[1] + cost
        heapq.heappush(heap, (dist[node[0]], node[0]))
  return dist

dists = []
ans = [0 for _ in range(N)]

for i in range(N):
  dists.append(distance(i))

for i in range(N):
  ans[i] = dists[i][X - 1] + dists[X - 1][i]

print(max(ans))
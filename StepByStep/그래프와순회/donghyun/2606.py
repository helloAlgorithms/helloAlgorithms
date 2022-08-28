import sys
from collections import deque

input = sys.stdin.readline
node, edge, start = int(input()), int(input()), 1
graph = [[] for _ in range(node + 1)]
for _ in range(edge):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)
q = deque([start])
visited = set([start])
computer = 0
while q:
    visit = q.popleft()
    for route in graph[visit]:
        if route not in visited:
            q.append(route)
            visited.add(route)
            computer += 1
print(computer)
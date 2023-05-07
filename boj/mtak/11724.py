from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0
for _ in range(m):
	f, t = map(int, input().split())
	graph[f].append(t)
	graph[t].append(f)
def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
for i in range(1, n + 1):
    if not visited[i]:
        if not graph[i]:
            visited[i] = True
        else:
            bfs(i)
        cnt += 1
print(cnt)

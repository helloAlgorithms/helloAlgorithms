import sys
sys.setrecursionlimit(10 ** 9)

def dfs(x, y):
    for a, b in graph[x]:
        if visited[a] == -1:
            visited[a] = b + y
            dfs(a, b + y)


v = int(sys.stdin.readline())

graph = [[] for _ in range(v + 1)]
for _ in range(v):
    w = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(w) - 2, 2):
        graph[w[0]].append([w[j], w[j + 1]])


visited = [-1] * (v + 1)
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))
visited = [-1] * (v + 1)
visited[start] = 0
dfs(start, 0)

print(max(visited))
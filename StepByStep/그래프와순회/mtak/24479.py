import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())#정점, 간선, 시작 정점
sys.setrecursionlimit(10**9)
V = [0] * (n + 1)# 정점 방문 집합
E = [[] for _ in range(n + 1)]#간선 집합
for _ in range(m):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)
cnt = 1
def dfs(s):
    global cnt
    V[s] = cnt
    E[s].sort()
    for i in E[s]:
        if not V[i]:
            cnt += 1
            dfs(i)

dfs(r)
for p in V[1:]:
    print(p)

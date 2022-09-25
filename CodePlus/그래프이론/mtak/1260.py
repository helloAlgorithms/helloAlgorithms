import sys
input = sys.stdin.readline
n, m, v = map(int, input().split())  # 정점 개수 , 간선 개수, 시작 번호
mm = [[0 for r in range(n + 1)] for c in range(n + 1)]
visit = [0 for _ in range(n + 1)]


def dfs(v):
    print(v, end=" ")
    visit[v] = 1
    for i in range(1, n + 1):
        if (visit[i] == 1 or mm[v][i] == 0):
            continue
        dfs(i)


def bfs(v):
    q = []
    q.append(v)
    visit[v] = 0
    while len(q) != 0:
        v = q[0]
        print(q[0], end=" ")
        q = q[1:]
        for i in range(1, n + 1):
            if (visit[i] == 0 or mm[v][i] == 0):
                continue
            q.append(i)
            visit[i] = 0


for _ in range(m):
    x, y = map(int, input().split())
    mm[x][y] = mm[y][x] = 1
dfs(v)
print()
bfs(v)

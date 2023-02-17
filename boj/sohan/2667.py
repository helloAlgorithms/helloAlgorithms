N = int(input())
m = [list(map(str, input())) for _ in range(N)]
n = 0

for _ in m:
    n += _.count('1')

v = [0 for _ in range(n)]
cs = []
adj = [[] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

index = 0
cnt = 0
ans = []

def visit(adj, i, v, cnt):
    v[i] = 1
    for a in adj[i]:
        if v[a] == 0:
            v[a] = 1
            cnt += 1
            cnt = visit(adj, a, v, cnt)
    return cnt

for i in range(N):
    for j in range(N):
        if m[i][j] == '1':
            cs.append([i - 1, j - 1])

for c in cs:
    x = c[0]
    y = c[1]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if [nx, ny] in cs:
            adj[index].append(cs.index([nx, ny]))
    index += 1

while 0 in v:
    cnt = visit(adj, v.index(0), v, cnt)
    ans.append(cnt)
    cnt = 0

ans.sort()
print(len(ans))
for _ in ans:
    print(_ + 1)

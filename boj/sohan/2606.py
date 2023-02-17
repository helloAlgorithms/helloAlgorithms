N = int(input())
M = int(input())
ls = [list(map(int, input().split())) for _ in range(M)]
es = [[] for i in range(N)]
v = [0] * N
c = 0

for l in ls:
    es[l[0] - 1].append(l[1] - 1)
    es[l[1] - 1].append(l[0] - 1)

def s(v, i, es, c):
    v[i] = 1
    for e in es[i]:
        if v[e] == 0:
            v[e] = 1
            c += 1
            c = s(v, e, es, c)
    return c

c = s(v, 0, es, c)
print(c)

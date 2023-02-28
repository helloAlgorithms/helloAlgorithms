import sys

N, M = map(int, input().split())
es = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
p = [-1 for i in range(N)]

def find(x):
    if p[x] < 0:
        return x

    p[x] = find(p[x])
    return p[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    
    if p[a] < p[b]:
        a, b = b, a
    
    p[b] += p[a]
    p[a] = b

for s, e in es:
    union(s - 1, e - 1)

print(sum(x < 0 for x in p))
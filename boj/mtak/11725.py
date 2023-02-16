import sys
from collections import deque
input = sys.stdin.readline
def f(n, tree):
    q = deque([1])
    parent = [0] *(n + 1)
    while q:
        now = q.popleft()
        for i in tree[now]:
            if parent[i] == 0 and i != 1:
                parent[i] = now
                q.append(i)
    for i in range(2, n + 1):
        print(parent[i])
cnt = int(input())
tree = dict()
for i in range(1, cnt + 1):
    tree[i] = []
for _ in range(cnt -1):
    n, nn = map(int, input().split())
    tree[n].append(nn)
    tree[nn].append(n)
f(cnt, tree)
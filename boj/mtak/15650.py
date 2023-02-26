import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pl = []
visited = 0
def printSet():
    for i in pl:
        print(i, end=" ")
    print()
def dfs(cnt):
    global visited
    if cnt == m:
        printSet()
        return 
    for i in range(1, n + 1):
        if visited & (1<<i):
            continue
        visited |= (1<<i)
        pl.append(i)
        dfs(cnt + 1)
        pl.pop()
        visited&=~(1<<i)
dfs(0)

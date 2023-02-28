import sys

N = int(input())
sched = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sched.sort(key = lambda x:(x[1], x[0]))
cnt = 1
s = sched.pop(0)[1]

for t in sched:
    if t[0] >= s:
        cnt += 1
        s = t[1]
    
print(cnt)

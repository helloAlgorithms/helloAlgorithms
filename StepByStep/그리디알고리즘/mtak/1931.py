import sys
input = sys.stdin.readline
N = int(input())
t = [list(map(int, input().split())) for _ in range(N)]
t = sorted(t, key=lambda a: a[0])
t = sorted(t, key=lambda a: a[1])
last = 0
cnt = 0
for i, j in t:
  if i >= last:
    cnt += 1
    last = j

print(cnt)
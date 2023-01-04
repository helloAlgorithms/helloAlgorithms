import sys
input = sys.stdin.readline
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
dx = 1
dy = 1
while (t):
    t -= 1
    dx *= (-1) if p + dx > w or p + dx < 0 else 1
    dy *= (-1) if q + dy > h or q + dy < 0 else 1
    p += dx
    q += dy
print(p, q)



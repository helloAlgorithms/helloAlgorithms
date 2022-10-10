import sys
input = sys.stdin.readline
cnt = int(input())
for _ in range(cnt):
    n, m = map(int, input().split(','))
    print(n + m)

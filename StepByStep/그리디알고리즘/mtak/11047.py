import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = [0] * n
for _ in range(n):
    a[_] = int(input())
cnt = 0
for i in range(n - 1, -1,-1):
    cnt += k // a[i]
    k %= a[i]
print(cnt)

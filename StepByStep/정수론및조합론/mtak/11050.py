import sys
n, k = map(int, input().split())
ret = 1
for i in range(n,n - k, -1):
    ret *= i
for i in range(k, 1, -1):
    ret /= i
print("%d"%ret)

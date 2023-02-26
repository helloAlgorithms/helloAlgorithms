import sys
input = sys.stdin.readline
n = int(input())
a = sorted(list(map(int, input().strip().split())))
b = sorted(list(map(int, input().strip().split())))
ret = 0
for idx, aa in enumerate(a):
    ret += aa * b[n - idx - 1]
print(ret)


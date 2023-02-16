import sys
input = sys.stdin.readline
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort(reverse=True)
_max = 0
for _ in range(n):
    if _max < a[_] * (_ + 1) :
        _max = a[_] * (_ + 1)
print(_max)

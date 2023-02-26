import sys
input = sys.stdin.readline
n = int(input())
_f = n // 5
while (n - _f * 5) % 3 != 0:
    _f -= 1
if _f < 0:
    print(-1)
    exit()
print(_f + (n - _f * 5) // 3)

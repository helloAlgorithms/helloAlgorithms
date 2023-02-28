import sys
n, s = map(int, input().split())
a = list(map(int, input().split()))
b = 0
e = 0
_sum = 0
l = sys.maxsize
while True:
    if e == n:
        break
    elif _sum >= s:
        l = min(l, e - b)
        _sum -= a[b]
        b += 1
    else:
        _sum += a[e]
        e += 1

print(0 if l == sys.maxsize else l)




import sys
input = sys.stdin.readline
c = input().split('-');
num = []
for p in c:
    sum = 0
    t = p.split('+')
    for pp in t:
        sum += int(pp)
    num.append(sum)
n = num[0]
for _ in num[1:]:
    n -= _
print(n)


import sys
input = sys.stdin.readline
cnt = int(input())
a = sorted([int(input()) for _ in range(cnt)])
re = [a[i] - a[i -1] for i in range(1, cnt)]
gcd = re[0]

def findGCD(div, num):
    rest = num % div
    while rest != 0:
        num, div = div, rest
        rest = num % div
    return div

for i in re[1:]:
    gcd = findGCD(gcd, i)
result = set()
for i in range(2, int(gcd**0.5) + 1):
    if gcd % i == 0:
        result.add(i)
        result.add(gcd // i)
result.add(gcd)
print(*sorted(list(result)))
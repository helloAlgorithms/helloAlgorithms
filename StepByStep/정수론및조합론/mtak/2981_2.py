import gc
from operator import ne
import sys
input = sys.stdin.readline
cnt = int(input())
start  = int(input())
next = int(input())
gcd = abs(start - next)

def getGCD(a, b):
    while b!= 0:
        a, b = b, a%b
    return a

def getCommonDivision(gcd):
    ret = set()
    for i in range(2, int(gcd**0.5) + 1):
        if gcd % i == 0:
            ret.add(i)
            ret.add(gcd // i)
    ret.add(gcd)
    return ret
for i in range(cnt - 2):
    start, next = next, int(input())
    gcd = getGCD(gcd, abs(start - next))
print(*sorted(list(getCommonDivision(gcd))))
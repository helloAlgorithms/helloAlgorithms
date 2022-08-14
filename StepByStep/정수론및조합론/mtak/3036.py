import sys
from fractions import Fraction
input = sys.stdin.readline
cnt = int(input())
radius = list(map(int,input().split()))
for i in range(cnt - 1):
    a = radius[0]
    b = radius[i + 1]
    while a%b  != 0:
        rest = a%b
        a, b = b, rest
    t = Fraction(radius[0], radius[i + 1])
    print(f"{t.numerator}/{t.denominator}")

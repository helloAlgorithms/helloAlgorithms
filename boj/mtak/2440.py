import sys
c = int(input())
a = "*"*c
for i in range(c):
    print(a[:(c - i)])

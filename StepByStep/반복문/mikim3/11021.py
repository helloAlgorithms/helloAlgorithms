# 11:45 시작

import sys
input = sys.stdin.readline
n = int(input())

total = 0
for i in range(n):
    a,b = map(int,input().split())
    total = a + b
    print("Case #%d: %d"%(i+1,total))

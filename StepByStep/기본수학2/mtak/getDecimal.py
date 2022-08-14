import sys
import math
a, b = map(int, sys.stdin.readline().split())
flag = -1
if a == 1:
    a += 1
for i in range(a, b + 1):
    flag = -1
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            flag = 1
            break
    if flag == -1:
        print(i)
import sys

N = int(input())
coor = list(map(int, sys.stdin.readline().split()))
coor_s = {item : i for i,item in enumerate(sorted(set(coor)))}

for c in coor:
    print(coor_s[c], end=" ")

import sys
x, y, w, h = map(int, sys.stdin.readline().split())
a = w-x
b = h - y
print(min(a,w,x,y))

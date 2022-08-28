import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
a = set(map(int, sys.stdin.readline().rstrip().split()))
b = set(map(int, sys.stdin.readline().rstrip().split()))

cnt = len(a - b)
cnt += len(b - a)
print(cnt)

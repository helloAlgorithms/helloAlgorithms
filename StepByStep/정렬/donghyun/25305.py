import sys

input = sys.stdin.readline
n, m = map(int, input().split())
print(sorted(map(int, input().split()))[-m])
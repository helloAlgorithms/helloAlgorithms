import sys

input = sys.stdin.readline
for _ in range(int(input())):
	n, m = map(int, input().split())
	[input() for _ in range(m)]
	print(n - 1)
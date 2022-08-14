import sys

input = sys.stdin.readline
n, m = map(int, input().split())
t = list(map(int, input().split()))
l, r = 0, max(t)
while l != r:
	lr = (l + r) // 2
	if sum([i - lr for i in t if i > lr]) >= m:
		l = lr + 1
	else:
		r = lr
print(l - 1)
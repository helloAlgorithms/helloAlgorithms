import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
graph = [1] * 100001
graph[n] = 0
x, t = n, 0
q = deque([(x, t)])
dp = {}
while x != k:
	x, t = q.popleft()
	for route in (x + 1, x - 1, x * 2):
		if 0 <= route <= 100000 and graph[route]:
			graph[route] = 0
			q.append((route, t + 1))
			dp[route] = x
track = [k]
while k != n:
	track.append(dp[k])
	k = dp[k]
print(t)
print(*track[::-1])
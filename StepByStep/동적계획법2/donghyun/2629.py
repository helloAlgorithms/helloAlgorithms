import sys

input = sys.stdin.readline
n, w = int(input()), list(map(int, input().split()))
c, t = int(input()), list(map(int, input().split()))
dp = [0] * 80001
dp[40000] = 1
for i in w:
	nxt = dp[:]
	for j in range(80001):
		if all([dp[j], j - i >= 0, j + i <= 80000]):
			nxt[j - i] = 1
			nxt[j + i] = 1
	dp = nxt[:]
print(*map(lambda x: 'Y' if dp[40000 + x] else 'N', t))
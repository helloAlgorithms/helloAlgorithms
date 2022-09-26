import sys

input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    dp[i] = max([dp[j] + 1 for j in range(i) if l[j] < l[i]] + [dp[i]])
lis = max(dp)
print(lis)
track = []
for i in range(n - 1, -1, -1):
	if dp[i] == lis:
		track.append(l[i])
		lis -= 1
print(*track[::-1])
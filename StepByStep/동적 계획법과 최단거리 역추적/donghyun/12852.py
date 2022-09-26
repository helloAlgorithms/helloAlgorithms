import sys

input = sys.stdin.readline
n = int(input())
dp = {1: 0, 2: 1, 3: 1}
track = []

def find(n):
	if n in dp:
		return dp[n]
	dp[n] = min(find(n//2) + n % 2, find(n//3) + n % 3) + 1
	return dp[n]

def tracker(n):
	track.append(n)
	if n == 1:
		return
	if n == 2:
		track.append(1)
		return
	div_by_2 = dp[n//2] + n % 2
	div_by_3 = dp[n//3] + n % 3
	if div_by_2 < div_by_3:
		if n % 2 == 1:
			track.append(n - 1)
		tracker(n // 2)
	else:
		for i in range(1, n % 3 + 1):
			track.append(n - i)
		tracker(n // 3)
print(find(n))
tracker(n)
print(*track)

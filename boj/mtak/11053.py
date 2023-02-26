n = int(input())
a = list(input().split())
ret = 0
mem = [0] * n
def dp(cnt):
	global ret
	dist = 0
	for i in range(cnt):
		if a[i] < a[cnt]:
			dist = max(dp
	dp[cnt] = dist + 1 
print(ret)

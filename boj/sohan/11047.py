N, K = map(int, input().split(" "))
coins = [int(input()) for _ in range(N)]
ans = 0

for num in reversed(coins):
	count = 1
	if num <= K:
		ans += K // num
		K = K % num	
	if K == 0:
		break

print(ans)
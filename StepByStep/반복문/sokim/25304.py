receipt = int(input())
cnt = int(input())
total = 0
for _ in range(cnt):
	price, n = map(int, input().split())
	total += price * n
if (receipt == total):
	print("Yes")
else:
	print("No")

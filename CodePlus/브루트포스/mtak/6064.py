import sys
input = sys.stdin.readline
cases = int(input())
for _ in range(cases):
	m, n, x, y = map(int, input().split())
	ans = x
	while not ((ans - x) % m == 0 and (ans - y) % n == 0):
		ans += m
		if ans > m * n:
			ans =  -1
			break
	print(ans)
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
p, a, b = 1000000007, 1, 1
for i in range(n - k + 1, n + 1):
	a = a * i % p
for i in range(1, k + 1):
	b = b * i % p
print(a * pow(b, p-2, p) % p)
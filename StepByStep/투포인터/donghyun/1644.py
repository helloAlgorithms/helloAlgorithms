import sys

input = sys.stdin.readline
n = int(input())
if n == 1:
	print(0)
	exit()
p, l = [], list(range(n + 1))
for i in range(2, n + 1):
	if l[i]:
		p.append(i)
		j = 2
		while i * j <= n:
			l[i * j] = 0
			j += 1
i, j, k, s = 0, 1, 0, p[0]
while i != j:
	if s > n:
		s -= p[i]
		i += 1
	elif s < n and j < len(p):
		s += p[j]
		j += 1
	else:
		if s == n:
			k += 1
		s -= p[i]
		i += 1
print(k)
import sys

input = sys.stdin.readline
n = int(input())
l = sorted(map(int, input().split()))
x = int(input())
i, j, k = 0, n - 1, 0
while i != j:
	s = l[i] + l[j]
	if s > x:
		j -= 1
	elif s < x:
		i += 1
	else:
		k += 1
		i += 1
print(k)
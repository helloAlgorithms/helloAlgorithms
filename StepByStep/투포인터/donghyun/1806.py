import sys

input = sys.stdin.readline
n, s = map(int, input().split())
l = list(map(int, input().split()))
i, j, k, c = 0, 1, float("inf"), l[0]
while i != j:
	if c >= s:
		k = min(k, j - i)
		c -= l[i]
		i += 1
	elif j == n:
		break
	else:
		c += l[j]
		j += 1
print(k if k != float("inf") else 0)
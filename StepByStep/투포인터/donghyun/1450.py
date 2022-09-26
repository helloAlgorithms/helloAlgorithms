import sys
from itertools import combinations
from bisect import bisect_right

input = sys.stdin.readline
n, c = map(int, input().split())
l = sorted(map(int, input().split()))
a, b = l[:len(l)//2], l[len(l)//2:]
a_sum, b_sum = [], []
for i in range(1, len(a) + 1):
	for j in combinations(a, i):
		a_sum.append(sum(j))
for i in range(1, len(b) + 1):
	for j in combinations(b, i):
		b_sum.append(sum(j))
a_sum, b_sum = sorted(a_sum), sorted(b_sum)
k = 1 + bisect_right(a_sum, c) + bisect_right(b_sum, c)
for i in a_sum:
	if i < c:
		k += bisect_right(b_sum, c - i)
print(k)
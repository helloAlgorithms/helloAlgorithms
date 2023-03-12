import sys

N, M = map(int, input().split(' '))
nums = list(map(int, sys.stdin.readline().split(' ')))
ranges = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(M)]
sums = [0]
summ = 0
for n in nums:
	summ += n
	sums.append(summ)

print(sums)

for x, y in ranges:
	print(sums[y] - sums[x - 1])
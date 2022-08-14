import sys
import bisect

input = sys.stdin.readline
int(input())
l = list(map(int, input().split()))
lis = [0]
for n in l:
	i = bisect.bisect_left(lis, n)
	if i < len(lis):
		lis[i] = n
	else:
		lis.append(n)
print(len(lis)-1)
import sys
import heapq

input = sys.stdin.readline
n = int(input())
l = sorted(map(int, input().split()))
i, j, k = 0, n - 1, []
while i != j:
	s = l[i] + l[j]
	heapq.heappush(k, (abs(s), (l[i], l[j])))
	if s > 0:
		j -= 1
	elif s < 0:
		i += 1
	else:
		print(l[i], l[j])
		exit()
print(*heapq.heappop(k)[1])
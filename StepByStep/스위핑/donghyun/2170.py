import sys

input = sys.stdin.readline 
n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()
start, end = lines[0]
answer = end - start
for x, y in lines:
	if start <= x and y <= end:
		continue
	answer += y - x - max(0, end - x)
	start, end = x, y
print(answer)
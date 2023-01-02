import sys

input = sys.stdin.readline 
n, m = map(int, input().split())
lines = []
for _ in range(n):
	x, y = map(int, input().split())
	if x > y:
		lines.append((-x, -y))
lines.sort()
start, end = lines[0]
answer = end - start
for x, y in lines:
	if start <= x and y <= end:
		continue
	answer += y - x - max(0, end - x)
	start, end = x, y
print(m + 2 * answer)
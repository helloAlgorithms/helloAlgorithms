import sys

input = sys.stdin.readline
n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
area = p[-1][0] * p[0][1] - p[0][0] * p[-1][1]
for i in range(n - 1):
	area += p[i][0] * p[i+1][1] - p[i+1][0] * p[i][1]
print(round(abs(area) / 2, 1))
import sys

N = int(sys.stdin.readline().rstrip())

# 좌표 리스트
points = list()
for _ in range(N):
	point = tuple(map(int, sys.stdin.readline().rstrip().split()))
	points.append(point)
points.sort()
for x, y in points:
	print(x, y)

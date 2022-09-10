import math

testcase = int(input())
for _ in range(testcase):
	# 출발점과 도착점
	x1, y1, x2, y2 = map(int, input().split())
	num = int(input())
	cnt = 0
	for _ in range(num):
		# 원의 중심과 반지름
		cx, cy, r = map(int, input().split())
		# 출발점~원의 중심까지의 거리
		d1 = math.sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)
		# 도착점~원의 중심까지의 거리
		d2 = math.sqrt((x2 - cx) ** 2 + (y2 - cy) ** 2)
		if ((d1 < r and d2 > r) or (d1 > r and d2 < r)):
			cnt += 1
	print(cnt)

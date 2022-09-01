import math

testcases = int(input())
for _ in range(testcases):
	x1, y1, r1, x2, y2, r2 = map(int, input().split())
	# 두 점 사이의 거리
	distance = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)

	# 원의 중심이 같고 반지름도 같은 경우
	if distance == 0 and r1 == r2:
		print(-1)
	# 내접 또는 외접인 경우
	elif distance == abs(r1 - r2) or distance == r1 + r2:
		print(1)
	# 서로 다른 두 점에서 만나는 원
	elif abs(r1 - r2) < distance < abs(r1 + r2):
		print(2)
	else:
		print(0)

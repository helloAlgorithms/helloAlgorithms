# 단위당 참외 개수
melon = int(input())
info = list()
# 큰 사각형의 가로 길이와 세로 길이
width = 0
height = 0
for _ in range(6):
	direction, length = map(int, input().split())
	info.append((direction, length))
for i, j in info:
	if i == 1 or i == 2:
		if j > width:
			width = j
	elif i == 3 or i == 4:
		if j > height:
			height = j
width_idx = [i[1] for i in info].index(width)
height_idx = [i[1] for i in info].index(height)
# 작은 사각형의 가로 길이와 세로 길이
sub_width = abs(info[(width_idx - 1) % 6][1] - info[(width_idx + 1) % 6][1])
sub_height = abs(info[(height_idx - 1) % 6][1] - info[(height_idx + 1) % 6][1])
# 도형의 넓이
area = width * height - sub_width * sub_height
print(melon * area)

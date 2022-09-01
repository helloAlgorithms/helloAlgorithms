# 좌표들의 리스트 [(x1, y1), (x2, y2) ...]
points = list()
for _ in range(3):
	points.append(tuple(map(int, input().split())))

dictionaryX = dict()
dictionaryY = dict()
for x, y in points:
	dictionaryX[x] = dictionaryX.get(x, 0) + 1
	dictionaryY[y] = dictionaryY.get(y, 0) + 1

for x, y in points:
	if dictionaryX[x] == 1:
		resultX = x
	if dictionaryY[y] == 1:
		resultY = y

print(resultX, resultY)

# (x, y): 현재 위치
# (w, h): 직사각형의 오른쪽 위 꼭지점
x, y, w, h = map(int, input().split())

# 직사각형의 경계선까지의 수직 거리들
distances = [x, y, w-x, h-y]
print(min(distances))

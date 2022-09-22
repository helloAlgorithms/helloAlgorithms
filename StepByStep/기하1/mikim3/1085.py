# 시작 시간 : 11:52
x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))




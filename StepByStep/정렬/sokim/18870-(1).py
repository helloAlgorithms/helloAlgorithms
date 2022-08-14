# 시간 초과됨
import sys

N = int(sys.stdin.readline().rstrip())
# 입력 받은 좌표 리스트
original = list(map(int, sys.stdin.readline().rstrip().split()))

# 크기 순으로 정렬
temp = original.copy()
temp.sort()

# 압축 좌표 리스트
compressed = list()
for number in original:
	pos = temp.index(number)
	compressed.append(pos)

for i in compressed:
	print(i, end = ' ')

import sys

N = int(sys.stdin.readline().rstrip())
# 입력 받은 좌표 리스트
original = list(map(int, sys.stdin.readline().rstrip().split()))

# 크기 순으로 정렬
temp = original.copy()
temp = list(set(temp))
temp.sort()

# 딕셔너리화
dic = {temp[i] : i for i in range(len(temp))}

# 압축 좌표 리스트
compressed = list()
for num in original:
	pos = dic[num]
	compressed.append(pos)

for i in compressed:
	print(i, end = ' ')

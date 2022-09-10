import sys

N = int(sys.stdin.readline().rstrip())
possession = list(map(int, sys.stdin.readline().rstrip().split())) # 가진 숫자 리스트
M = int(sys.stdin.readline().rstrip())
question = list(map(int, sys.stdin.readline().rstrip().split())) # 검사할 숫자 리스트

dic = dict() # 딕셔너리화
for i in possession:
	dic[i] = dic.get(i, 0) + 1

for i in question:
	cnt = dic.get(i, 0)
	print(cnt, end = ' ')

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
possession = list() # 도감 리스트
question = list() # 질문 리스트
for _ in range(N):
	possession.append(sys.stdin.readline().rstrip())
for _ in range(M):
	question.append(sys.stdin.readline().rstrip())

dic = {possession[i] : i + 1 for i in range(N)} # '포켓몬 이름' : 번호 딕셔너리화
for i in question:
	if i.isdigit() is True:
		print(possession[int(i) - 1])
	else:
		print(dic[i])

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
possession = list() # 가진 문자열
question = list() # 검사할 문자열
for _ in range(N):
	possession.append(sys.stdin.readline().rstrip())
for _ in range(M):
	question.append(sys.stdin.readline().rstrip())

dic = {x : 1 for x in possession} # 딕셔너리화
cnt = 0 # 정답
for i in question:
	cnt += dic.get(i, 0)
print(cnt)

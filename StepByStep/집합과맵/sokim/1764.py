import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
a = dict()
b = dict()
for _ in range(N):
	i = sys.stdin.readline().rstrip()
	a[i] = 1
for _ in range(M):
	i = sys.stdin.readline().rstrip()
	b[i] = 1

cnt = 0 # 듣보잡의 수
array = list() # 듣보잡 리스트
for i in a:
	if b.get(i, 0) == 1:
		cnt += 1
		array.append(i)

array.sort()
print(cnt)
for i in array:
	print(i)

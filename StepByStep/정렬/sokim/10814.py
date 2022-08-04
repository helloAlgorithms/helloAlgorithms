import sys

N = int(sys.stdin.readline().rstrip())

# 회원 리스트
members = list()
for _ in range(N):
	age, name = sys.stdin.readline().rstrip().split()
	age = int(age)
	members.append((age, name))

# 나이 순으로 정렬
members.sort(key = lambda x: x[0])
for member in members:
	print(member[0], member[1])

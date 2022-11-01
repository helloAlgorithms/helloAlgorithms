case = int(input())
for _ in range(case):
	tmp = input().split()
	for p in tmp:
		print(p[::-1], " ", end="")

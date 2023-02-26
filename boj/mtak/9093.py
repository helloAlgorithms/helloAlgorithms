case = int(input())
for _ in range(case):
	tmp = input().split()
	for idx, i in enumerate(tmp):
		tmp[idx] = "".join(reversed(i))
	print(" ".join(tmp))

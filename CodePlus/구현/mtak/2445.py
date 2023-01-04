s = int(input())
for i in range(0, s):
	print("*"*(i + 1) + " " * 2 *(s - i - 1) + "*" * (i + 1))
for i in range(s - 2, -1, -1):
	print("*"*(i + 1) + " " * 2 *(s - i - 1) + "*" * (i + 1))

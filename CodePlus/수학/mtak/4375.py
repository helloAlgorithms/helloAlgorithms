import sys
input = sys.stdin.readline
while True:
	start = 0
	try:
		i = int(input())
	except:
		break
	f = 1
	while True:
		start = start * 10 + 1
		start %= i
		if start == 0:
			print(f)
			break
		f += 1

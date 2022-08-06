# 시간 초과
import sys

N = int(sys.stdin.readline().rstrip())
possession = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline().rstrip())
question = list(map(int, sys.stdin.readline().rstrip().split()))

for i in question:
	if i in possession:
		print(1, end = ' ')
	else:
		print(0, end = ' ')

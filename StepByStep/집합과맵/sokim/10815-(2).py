import sys

N = int(sys.stdin.readline().rstrip())
possession = list(map(int, sys.stdin.readline().rstrip().split()))
dic = {i : 1 for i in possession}

M = int(sys.stdin.readline().rstrip())
question = list(map(int, sys.stdin.readline().rstrip().split()))

for i in question:
	cnt = dic.get(i, 0)
	print(cnt, end = ' ')

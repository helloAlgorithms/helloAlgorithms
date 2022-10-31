import copy
while True:
	s = input().strip()
	if s == '0':
		break
	ss = copy.deepcopy(s)[::-1]
	flag = 0
	for idx, p in enumerate(s):
		if p != ss[idx]:
			print('no')
			flag = 1
			break
	if flag == 0:	print('yes')

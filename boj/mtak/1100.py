cnt = 0
lines = []
flag = 0
for _ in range(8):
	lines.append(input().strip())
	
for line in lines:
	line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
	if line == "":
		print(cnt)
		exit()
	for p in line[flag::2]:
		if p != '.':
			cnt += 1
	flag = 1 if flag == 0 else 0
print(cnt)


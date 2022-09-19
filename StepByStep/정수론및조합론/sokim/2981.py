import sys

cnt = int(sys.stdin.readline().rstrip())
nums = list()
for _ in range(cnt):
	nums.append(int(sys.stdin.readline().rstrip()))

for i in range(2, nums[0] + 1):
	# 나머지가 모두 같은지 알려주는 플래그
	flag = True
	prev = nums[0] % i
	for num in nums:
		now = num % i
		if prev != now:
			flag = False
			break
	if flag == True:
		print(i, end = ' ')

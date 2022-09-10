import sys

while True:
	# 삼각형의 변 길이 리스트
	nums = list(map(int, sys.stdin.readline().rstrip().split()))
	if nums[0] == 0 and nums[1] == 0 and nums[2] == 0:
		quit()
	# 빗변의 길이(직각 삼각형이 아닌 경우 가장 긴 변의 길이)
	longest = max(nums)
	nums.remove(longest)
	if longest ** 2 == nums[0] ** 2 + nums[1] ** 2:
		print("right")
	else:
		print("wrong")

import copy
from collections import deque

def solution(queue1, queue2):
	copy_q1 = copy.deepcopy(queue1)
	copy_q2 = copy.deepcopy(queue2)

	q1 = deque(queue1)
	q2 = deque(queue2)
	total1 = sum(q1)
	total2 = sum(q2)
	limit = (len(queue1)) * 4

	ans = 0
	total_sum = sum(q1) + sum(q2)
	if total_sum % 2 != 0:
		return -1
	
	while 1:
		if total1 > total2:
			buf = q1.popleft()
			q2.append(buf)
			total1 -= buf
			total2 += buf
			ans += 1
		elif total1 < total2:
			buf = q2.popleft()
			q1.append(buf)
			total1 += buf
			total2 -= buf
			ans += 1
		else:
			break
		if ans == limit:
			return -1
	return ans

print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
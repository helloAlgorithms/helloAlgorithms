# 모든 차량이 고속도로를 이용하면서 카메라 한 번은 만나도록
# 최소 몇 대의 카메라를 설치해야 하는지
def solution(routes):
	answer = 0

	now = -30001

	routes.sort(key= lambda x: x[1])
	for i in range(len(routes)):
		if routes[i][0] <= now:
			continue
		else:
			answer += 1
			now = routes[i][1]

	return answer

solution([
	# 진입, 진출
	[-20, -15], 
	[-14, -5], 
	[-18, -13], 
	[-5, -3]
])

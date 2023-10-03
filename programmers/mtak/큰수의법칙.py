def solution(firstLine, secondLine):
	n, m, k = map(int, firstLine.split())
	arr = list(map(int, secondLine.split()))
	arr.sort(reverse=True)
	print(arr)
	answer = 0

	while m > 0:
		for _ in range(k):
			if m == 0:
				break
			answer += arr[0]
			print(arr[0])
			m -= 1
		if m > 0 :
			answer += arr[1]
			print(arr[1])
			m -= 1
	return answer
	"""
	answer에 선빵을 최대한 더한다 [9,3]
	부관이 같다면 선빵처럼 최대한 더라고 000 000 000 , 000 0 000 0 0
	부관이 다르면 하나만 살포시 끼운다
	"""


if __name__ == '__main__':
	print(solution("5 8 3", "2 4 5 4 6"))
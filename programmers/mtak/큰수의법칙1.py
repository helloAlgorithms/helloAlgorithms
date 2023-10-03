def solution(firstLine, secondLine):
	n, m, k = map(int, firstLine.split())
	arr = list(map(int, secondLine.split()))
	arr.sort(reverse=True)
	answer = 0
	제일큰숫자개수 = m // (k + 1) * k + m % (k + 1)
	두번째로큰숫자개수 = m - 제일큰숫자개수
	answer = arr[0] * 제일큰숫자개수 + arr[1] * 두번째로큰숫자개수
	return answer

if __name__ == '__main__':
	print(solution("5 8 3", "2 4 5 4 6"))
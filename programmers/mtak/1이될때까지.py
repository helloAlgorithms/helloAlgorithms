def solution(firstLine):
	n, k = map(int, firstLine.split())
	result = 0
	while n != 1:
		while n % k > 0:
			n -= 1
			result += 1
		n //= k
		result += 1
	return result


def solution1(firstLine):
	n, k = map(int, firstLine.split())
	result = 0
	while True:
		target = (n//k) * k
		result += (n - target)
		n = target
		if n < k:
			break
		result += 1
		n //= k
	print(n)
	result += (n - 1)
	return result

def test_solution():
	assert solution1("25 5") == 2

print(solution1("25 5"))
def solution(firstLine, secondLine):
	n, m = map(int, firstLine.split())
	chart = [ [int(c) for c in r.split()] for r in secondLine.split("\n")]
	answer = 0
	for r in chart:
		candidate = min(r)
		if answer < candidate: answer = candidate
	return answer

def test_solution():
	assert solution("3 3", """3 1 2
4 1 4
2 2 2""") == 2

def test_solution2():
	assert solution("2 4","""7 3 1 8
3 3 3 4""") == 3
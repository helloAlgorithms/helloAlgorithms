import sys
from math import sqrt
from itertools import permutations

input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
	s = (x1 - x2) * (y1 - y3) - (x1 - x3) * (y1 - y2)
	return 1 if s > 0 else -1 if s < 0 else 0

def convert(i, length):
	diag = length/sqrt(2)
	if i == 0:
		return (0, length)
	elif i == 1:
		return (diag, diag)
	elif i == 2:
		return (length, 0)
	elif i == 3:
		return (diag, -diag)
	elif i == 4:
		return (0, -length)
	elif i == 5:
		return (-diag, -diag)
	elif i == 6:
		return (-length, 0)
	elif i == 7:
		return (-diag, diag)

if __name__ == "__main__":
	l = list(map(int, input().split()))
	n = len(l)
	total = 0
	for case in permutations(l, n):
		p = [convert(i, j) for i, j in enumerate(case)]
		for i in range(n):
			direction = ccw(*p[i % n], *p[(i + 1) % n], *p[(i + 2) % n])
			if direction != -1:
				break
		else:
			total += 1
	print(total)
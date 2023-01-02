import sys

input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
	s = (x1 - x2) * (y1 - y3) - (x1 - x3) * (y1 - y2)
	return 1 if s > 0 else -1 if s < 0 else 0

if __name__ == "__main__":
	x1, y1 = map(int, input().split())
	x2, y2 = map(int, input().split())
	x3, y3 = map(int, input().split())
	print(ccw(x1, y1, x2, y2, x3, y3))
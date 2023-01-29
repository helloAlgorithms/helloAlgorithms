import sys

input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
	s = (x1 - x2) * (y1 - y3) - (x1 - x3) * (y1 - y2)
	return 1 if s > 0 else -1 if s < 0 else 0

if __name__ == "__main__":
	ax, ay, bx, by = map(int, input().split())
	cx, cy, dx, dy = map(int, input().split())
	A, B, C, D = (ax, ay), (bx, by), (cx, cy), (dx, dy)
	if ccw(*A, *B, *C) * ccw(*A, *B, *D) < 0 and \
	ccw(*C, *D, *A) * ccw(*C, *D, *B) < 0:
		print(1)
	else:
		print(0)
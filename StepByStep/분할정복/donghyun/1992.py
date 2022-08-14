import sys

input = sys.stdin.readline
n = int(input())
l = [input().strip() for _ in range(n)]
def dq(x, y, n):
	color = l[x][y]
	for i in range(x, x + n):
		for j in range(y, y + n):
			if color != l[i][j]:
				dq.result += "("
				dq(x, y, n//2)
				dq(x, y + n//2, n//2)
				dq(x + n//2, y, n//2)
				dq(x + n//2, y + n//2, n//2)
				dq.result += ")"
				return
	dq.result += color
dq.result = ""
dq(0, 0, n)
print(dq.result)
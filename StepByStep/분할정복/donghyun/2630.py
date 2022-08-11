import sys

input = sys.stdin.readline
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
paper = [0, 0]
def dq(x, y, n):
	color = l[x][y]
	for i in range(x, x + n):
		for j in range(y, y + n):
			if color != l[i][j]:
				dq(x, y, n//2)
				dq(x + n//2, y, n//2)
				dq(x, y + n//2, n//2)
				dq(x + n//2, y + n//2, n//2)
				return
	paper[color] += 1
dq(0, 0, n)
print(*paper)
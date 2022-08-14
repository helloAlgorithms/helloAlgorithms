import sys

input = sys.stdin.readline
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
result = [0, 0, 0]
def dq(x, y, n):
	num = l[x][y]
	for i in range(x, x + n):
		for j in range(y, y + n):
			if num != l[i][j]:
				dq(x, y, n//3)
				dq(x, y + n//3, n//3)
				dq(x, y + n//3*2, n//3)
				dq(x + n//3, y, n//3)
				dq(x + n//3, y + n//3, n//3)
				dq(x + n//3, y + n//3*2, n//3)
				dq(x + n//3*2, y, n//3)
				dq(x + n//3*2, y + n//3, n//3)
				dq(x + n//3*2, y + n//3*2, n//3)
				return
	result[num] += 1
dq(0, 0, n)
print(result[-1], result[0], result[1])
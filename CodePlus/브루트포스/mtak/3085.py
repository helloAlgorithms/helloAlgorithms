import sys
input = sys.stdin.readline
N = int(input())
M = [list(input()) for _ in range(N)];
D = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ans = 0
def maxCandy():
    rowCnt, colCnt, rowMax, colMax = 0, 0,-1e9, -1e9
    for i in range(N):
        for j in range(N - 1):
            if M[i][j] == M[i][j + 1]:
                rowCnt += 1
            else:
                rowCnt = 1
            rowMax = max(rowCnt,rowMax)
        rowCnt = 1
    for j in range(N):
        for i in range(N - 1):
            if M[i][j] == M[i + 1][j]:
                colCnt += 1
            else:
                colCnt = 1
            colMax = max(colCnt, colMax)
        colCnt = 1
    return max(rowMax, colMax)

for i in range(N):
	for j in range(N):
		for k in range(4):
			nx = i + D[k][0]
			ny = j + D[k][1]
			if (nx < 0 or nx >= N or ny < 0 or ny >= N):
				continue
			if (M[i][j] != M[nx][ny]):
				M[i][j],M[nx][ny] = M[nx][ny],M[i][j]
				ans = max(ans, maxCandy())
				M[i][j],M[nx][ny] = M[nx][ny],M[i][j]
print(ans)

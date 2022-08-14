import sys
input = sys.stdin.readline
N = int(input())
m = ""
for _ in range(N):
	m += input().strip()
maxCnt = 0
for i in range(N * N - 1):
	for j in range(i + 1, N * N):
		for k in range(0,N * (N - 1)):
			for l in range(0, N):
				t = N[l]
				for m in range(l + 3, N, 3):
					if N[m] != N[l] or m + 3 > N:
						candidate = len(t)
						if candidate >maxCnt:
							maxCnt = candidate
						continue
					t += N[m]
				p = N[l]
				for m in range(

				


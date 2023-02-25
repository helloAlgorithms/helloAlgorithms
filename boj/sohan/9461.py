T = int(input())

P = [0 for i in range(102)]

P[1], P[2], P[3] = 1, 1, 1
P[4], P[5] = 2, 2
P[6] = 3
P[7] = 4
P[8] = 5
P[9] = 7
P[10] = 9

for i in range(11, 102):
	P[i] = P[i - 1] + P[i - 5]

for _ in range(T):
	N = int(input())
	print(P[N])
from collections import deque

T = int(input())

def D(old):
	new = 2 * old
	if new > 9999:
		new = new % 10000
	
	return new

def S(old):
	if old == 0:
		return 9999
	new = old - 1

	return new

def L(old):
	begin = old % 1000
	end = old // 1000

	return begin * 10 + end

def R(old):
	begin = old % 10
	end = old // 10

	return begin * 1000 + end

def bfs(A, B):
	q = deque()
	check = set()
	q.append((A, ""))
	check.add(A)
	while q:
		num, op = q.popleft()
		if num == B:
			print(op)
			return
		
		nD = D(num)
		if nD not in check:
			q.append((nD, op + "D"))
			check.add(nD)
		
		nS = S(num)
		if nS not in check:
			q.append((nS, op + "S"))
			check.add(nS)

		nL = L(num)
		if nL not in check:
			q.append((nL, op + "L"))
			check.add(nL)

		nR = R(num)
		if nR not in check:
			q.append((nR, op + "R"))
			check.add(nR)

for _ in range(T):
	A, B = map(int, input().split())
	bfs(A, B)

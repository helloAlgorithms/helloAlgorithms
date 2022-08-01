import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
q = deque(range(1, n + 1))
l = map(int, input().split())
c = 0
for i in l:
	d = -1 if len(q)//2 >= q.index(i) else 1
	while q[0] != i:
		q.rotate(d)
		c += 1
	q.popleft()
print(c)
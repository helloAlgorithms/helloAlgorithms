import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [0] * 101
warp = [0] * 101
for _ in range(n + m):
	f, t = map(int, input().split())
	warp[f] = t
q = deque([1])
q_next = deque()
graph[1] = 0
c = 1
while q:
	visit = q.popleft()
	for i in range(1, 7):
		move = visit + i
		if move < 101 and graph[move] == 0:
			graph[move] = c
			if warp[move]:
				move, graph[warp[move]] = warp[move], c
			q_next.append(move)
	if not q:
		q, q_next, c = q_next, deque(), c + 1
print(graph[100])
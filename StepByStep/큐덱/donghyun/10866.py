import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
q = deque()
for _ in range(n):
	cmd = input()
	if cmd.startswith("push_front"):
		q.appendleft(int(cmd.split()[1]))
	elif cmd.startswith("push_back"):
		q.append(int(cmd.split()[1]))
	elif cmd.startswith("pop_front"):
		print(q.popleft() if len(q) else -1) 
	elif cmd.startswith("pop_back"):
		print(q.pop() if len(q) else -1) 
	elif cmd.startswith("size"):
		print(len(q))
	elif cmd.startswith("empty"):
		print(int(len(q)==0))
	elif cmd.startswith("front"):
		print(q[0] if len(q) else -1)
	elif cmd.startswith("back"):
		print(q[-1] if len(q) else -1)
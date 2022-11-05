# 시작시간 18:43  19:14  
# 큐의 어디가 앞이고 어디가 뒤인지가 너무 헷갈렸다.
# 큐의 앞 == popleft값 == 

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()
for i in range(n):
    cmd = list(map(str, input().split()))
    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            tmp = queue.popleft()
            queue.appendleft(tmp)
            print(tmp)    
    elif cmd[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            tmp = queue.pop()
            queue.append(tmp)
            print(tmp)
        
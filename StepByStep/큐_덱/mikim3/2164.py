# 시작시간 19:45

from collections import deque

n = int(input())


queue = deque() 
for i in range(1,n+1):
    queue.append(i)


while len(queue) != 1:
    queue.popleft()
    tmp = queue.popleft()
    queue.append(tmp)

print(queue.pop())


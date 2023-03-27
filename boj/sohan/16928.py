from collections import deque

N, M = map(int, input().split(' '))
board = [i for i in range(0, 101)]
ladders = dict()
snakes =dict()

for _ in range(N):
    a, b = map(int, input().split(' '))
    ladders[a] = b

for _ in range(M):
    a, b = map(int, input().split(' '))
    snakes[a] = b

count = 0

q = deque()
q.append((1, count))
visited = [0 for i in range(101)]
while q:
    num, count = q.popleft()
    for i in range(1, 7):
        num_next = num + i
        if num_next == 100:
            print(count + 1)
            exit(0)
        if num_next > 100:
            continue
        if num_next in ladders:
            num_next = ladders[num_next]
        elif num_next in snakes:
            num_next = snakes[num_next]
        
        if not visited[num_next]:
            q.append((num_next, count + 1))
            visited[num_next] = 1
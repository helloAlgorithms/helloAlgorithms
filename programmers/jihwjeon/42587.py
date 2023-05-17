from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([])
    for i, p in enumerate(priorities):
        q.append([p, i])
        
    while q:
        if q[0][0] == max(q)[0]:
            answer += 1
            v, i = q.popleft()
            if i == location:
                break
        else:
            x = q.popleft()
            q.append(x)
                
    return answer

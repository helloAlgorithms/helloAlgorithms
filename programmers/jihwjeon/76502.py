from collections import deque

def check_validate(s):
    arr = []
    
    for c in s:
        if c == ']' or c == '}' or c == ')':
            if not arr:
                return False
            if c == ']' and arr[-1] != '[':
                return False
            if c == '}' and arr[-1] != '{':
                return False
            if c == '(' and arr[-1] != '(':
                return False
            arr.pop()
        else:
            arr.append(c)
    if arr:
        return False
    return True

def solution(s):
    answer = 0
    
    s = deque(list(s))
    for _ in range(len(s)):
        if check_validate(s):
            answer += 1
        tmp = s.popleft()
        s.append(tmp)
    
    return answer

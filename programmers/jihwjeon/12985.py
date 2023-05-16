def solution(n,a,b):
    answer = 1
    a -= 1
    b -= 1
    
    while a // 2 != b // 2:
        a //= 2
        b //= 2
        answer += 1
    
    return answer

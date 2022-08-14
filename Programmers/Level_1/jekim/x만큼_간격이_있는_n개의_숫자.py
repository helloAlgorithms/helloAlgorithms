# def solution(x, n):
#     answer = []
#     for i in range(n): answer.append(x * (i + 1))  
#     return answer

def solution(x, n): return [(i * x) + x for i in range(n)]
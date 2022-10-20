def solution(A,B):
    return ((A + B) * (A - B))

A,B = map(int, input().split(' '))
print(solution(A, B))

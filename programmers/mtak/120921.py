def solution(A, B):
    tmp = A
    cnt = 0
    for i in range(len(A)):
        if A == B:
            return cnt
        A = A[-1] + A[:-1]
        cnt += 1
    return -1

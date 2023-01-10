def solution(M, N):
    answer = min(M - 1 + M *(N - 1), N - 1 + N * (M - 1))
    return answer

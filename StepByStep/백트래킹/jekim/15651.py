import sys

def dfs(answer: list, s : list, M : int, N : int):
    if len(s) == M:
        return answer.append(" ".join(map(str, s)))
    for i in range(1, N+1):
        s.append(i)
        dfs(answer, s, M, N)
        s.pop()

def solution(N, M):
    answer = []
    s = []
    dfs(answer, s, M, N)
    return answer

def print_answer_list(answer_list: list) -> None:
    for answer in answer_list: print(answer)

def runtime() -> None:
    N, M = map(int, sys.stdin.readline().split())
    print_answer_list(solution(N, M))

runtime()
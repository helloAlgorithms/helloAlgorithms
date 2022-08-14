import sys

def dfs(answer: list, s : list, source_list: list, M : int, N : int):
    if len(s) == M:
        return answer.append(" ".join(map(str, s)))
    for i in source_list:
        if i not in s:
            s.append(i)
            dfs(answer, s, source_list, M, N)
            s.pop()

def solution(N, M, source_list):
    answer = []
    s = []
    source_list.sort()
    dfs(answer, s, source_list, M, N)
    return answer

def print_answer_list(answer_list: list) -> None:
    for answer in answer_list: print(answer)

def runtime() -> None:
    N, M = map(int, sys.stdin.readline().split())
    source_list = list(map(int, sys.stdin.readline().split()))
    print_answer_list(solution(N, M, source_list))

runtime()

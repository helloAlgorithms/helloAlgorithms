from cProfile import run
import sys

def dfs(s : list, M : int, N : int):
    if len(s) == M:
        print(" ".join(map(str, s)))
        return
    for i in range(1, N+1):
        if i not in s:
            s.append(i)
            dfs(s, M, N)
            s.pop() 

def solution(N, M):
    answer = []
    s = []
    dfs(s, M, N)
    return 

def runtime() -> None:
    N, M = map(int, sys.stdin.readline().split())
    solution(N, M)

runtime()
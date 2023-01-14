# Title: 안전 영역
# Link: https://www.acmicpc.net/problem/2468

import sys
from enum import Enum
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**6)

def bfs(board: list, visited: list, x: int, y: int, num: int, N: int) -> None:
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        i, j = q.popleft()
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < N and 0 <= y < N and board[x][y] >= num and not visited[x][y]:
                visited[x][y] = True
                q.append((x, y))

def solution(board: list, N: int) -> int:
    heights = []
    for i in range(N):
        for j in range(N):
            if board[i][j] not in heights:
                heights.append(board[i][j])
    results = []
    for num in heights:
        cnt = 0
        visited = [[False for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] >= num and not visited[i][j]:
                    bfs(board, visited, i, j, num, N)
                    cnt += 1
        results.append(cnt)
    return max(results)

def get_input_geometry(N : int) -> list:
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    return board

def main() -> None:
    N = int(input())
    board = get_input_geometry(N)
    print(solution(board, N))
    return

if __name__ == "__main__":
    main()
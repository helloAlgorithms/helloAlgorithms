# Title: 연구소
# Link: https://www.acmicpc.net/problem/14502
# 시간조건으로 인해 pypy3로 통과
from copy import deepcopy

empty = 0
wall = 1
virus = 2
max_count = 0

class queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def is_empty(self):
        return len(self.items) == 0

def get_empty_count(lab: list, N: int, M: int) -> int:
    count = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j] == empty:
                count += 1
    return count

def check_virus_position(lab: list, Q : queue, N: int, M: int) -> None:
    for i in range(N):
        for j in range(M):
            if lab[i][j] == virus:
                Q.enqueue((i, j))
    return

def spread_virus(lab: list, N: int, M: int) -> None:
    after_spread = deepcopy(lab)
    q = queue()
    check_virus_position(after_spread, q, N, M)
    while not q.is_empty():
        x, y = q.dequeue()
        for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= i < N and 0 <= j < M and after_spread[i][j] == empty:
                after_spread[i][j] = virus
                q.enqueue((i, j))
    empty_count = get_empty_count(after_spread, N, M)
    global max_count
    max_count = max(max_count, empty_count)
    

def make_wall(lab: list, N: int, M: int, wall_count: int) -> None:
    if wall_count == 3:
        spread_virus(lab, N, M)
        return
    for i in range(N):
        for j in range(M):
            if lab[i][j] == empty:
                lab[i][j] = wall
                make_wall(lab, N, M, wall_count + 1)
                lab[i][j] = empty
    return

def solution(lab: list, N: int, M: int) -> int:
    temp_lab = deepcopy(lab)
    for i in range(N):
        for j in range(M):
            if lab[i][j] == empty:
                temp_lab[i][j] = wall
                make_wall(temp_lab, N, M, 1)
                temp_lab[i][j] = empty
    return max_count


def main():
    N, M = map(int, input().split())
    lab = []
    for _ in range(N):
        lab.append(list(map(int, input().split())))
    print(solution(lab, N, M))
    return

if __name__ == "__main__":
    main()
import sys
import copy
input = sys.stdin.readline

def check(lines: list, mid: int, line_cnt: int, line_length: int) -> bool:
    cnt = 0
    copied = copy.deepcopy(lines)
    for i in copied:
        cnt += i // mid
    return True if cnt >= line_length else False

def solution(lines: list, line_cnt: int, line_length: int) -> int:
    lines.sort()
    start = 1
    answer = 0
    end = max(lines)
    while start <= end:
        mid = (start + end) // 2
        if check(lines, mid, line_cnt, line_length) == True:
            if mid > answer: answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer


def runtime() -> None:
    line_cnt, line_length = map(int, input().split())
    lines = []
    for _ in range(line_cnt): lines.append(int(input().rstrip()))
    print(solution(lines, line_cnt, line_length))

if __name__ == "__main__": runtime()
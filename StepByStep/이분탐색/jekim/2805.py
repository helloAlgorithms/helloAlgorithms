import sys
input = sys.stdin.readline

def determin(woods_list : list, mid : int, needed_length : int) -> bool:
    sum = 0
    for i in woods_list:
        if i > mid: sum += (i - mid)
    return True if sum >= needed_length else False

def solution(woods_list : list, needed_length : int) -> int:
    woods_list.sort()
    start = 0
    end = max(woods_list)
    while start <= end:
        mid = (start + end) // 2
        if determin(woods_list, mid, needed_length) == True:
            start = mid + 1
        else:
            end = mid - 1       
    return end

def runtime() -> None:
    woods_cnt, needed_length = map(int, input().split())
    woods_list = list(map(int, input().split()))
    print(solution(woods_list, needed_length))

runtime()
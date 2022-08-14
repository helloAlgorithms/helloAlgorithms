import sys

def solution(closet: dict, clothes_cnt : int) -> int:
    answer = 1
    for type in closet:
        answer *= len(closet[type])
    return answer - 1

def runtime() -> None:
    case_cnt = int(sys.stdin.readline())
    for _ in range(case_cnt):
        clothes_cnt = int(sys.stdin.readline())
        closet = {}
        for _ in range(clothes_cnt):
            name, type = sys.stdin.readline().split()
            if type not in closet: closet[type] = ["Null"]
            closet[type].append(name)
        print(solution(closet, clothes_cnt))

runtime()

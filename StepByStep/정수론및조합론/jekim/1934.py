import sys

def gcd(a : int, b : int) -> int: return a if b == 0 else gcd(b, a % b)

def solution(a : int, b : int) -> int:
    return a * b // gcd(a, b)

def runtime() -> None:
    case_cnt = int(input())
    for _ in range(case_cnt):
        a, b = map(int, input().split())
        print(solution(a, b))

runtime()
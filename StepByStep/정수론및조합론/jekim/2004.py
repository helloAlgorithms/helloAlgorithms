import sys

# 메모리 초과
# 펙토리얼을 사용했을 때엔 숫자의 범위 때문에 메모리 초과가 발생한다.
# def get_Comp_list(a : int, b : int) -> list:
#     ret = [1]
#     for i in range(1, max(a, b) + 1): ret.append(i * ret[i - 1])
#     return ret

# def bino_coeff(n : int, r : int, fact_list : list) -> int:
#     return fact_list[n] // fact_list[n - r] // fact_list[r]

# def solution(a : int, b : int) -> int:
#     dp_list = get_Comp_list(a, b)
#     target = bino_coeff(a, b, dp_list)
#     answer = 0
#     while True:
#         if target % 10 == 0:
#             target //= 10
#             answer += 1
#         else:
#             break
#     return answer

def count_two_coefficient(n : int) -> int:
    answer = 0
    while n != 0:
        n = n // 2
        answer += n
    return answer

def count_five_coefficient(n : int) -> int:
    answer = 0
    while n != 0:
        n = n // 5
        answer += n
    return answer

def solution(a : int, b : int) -> int:
    two_cnt = count_two_coefficient(a) - count_two_coefficient(a - b) - count_two_coefficient(b)
    five_cnt = count_five_coefficient(a) - count_five_coefficient(a - b) - count_five_coefficient(b)
    return min(two_cnt, five_cnt)

def runtime() -> None:
    a, b = map(int, sys.stdin.readline().split())
    print(solution(a, b))

runtime()
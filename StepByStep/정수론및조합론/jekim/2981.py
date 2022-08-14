import sys

# def Euclidean_algorithm(a : int, b : int) -> int:
#     if (b == 0): return a
#     else: return Euclidean_algorithm(b, a % b)

def get_gcd(a : int, b : int) -> int: return a if b == 0 else get_gcd(b, a % b)

def solution(paper_list : list, paper_cnt : int) -> list:
    answer = set()
    re_num_list = []
    paper_list.sort()
    for i in range(1, paper_cnt):
        re_num_list.append(paper_list[i] - paper_list[i - 1])
    gcd = re_num_list[0]
    for i in range(1, len(re_num_list)):
        gcd = get_gcd(gcd, re_num_list[i])
    for i in range(2, int(gcd ** 0.5) + 1):
        if gcd % i == 0:
            answer.add(i)
            answer.add(gcd // i)
    answer.add(gcd)
    return list(answer)

# def print_elements_list_with_a_line(lst : list) -> None:
#     for i in lst:
#         if (i == lst[-1]): print(i)
#         else: print(i, end = ' ')

def runtime() -> None:
    paper_cnt = int(sys.stdin.readline().rstrip())
    paper_list = sorted([int(sys.stdin.readline().rstrip()) for _ in range(paper_cnt)])
    print(*sorted(solution(paper_list, paper_cnt)))

runtime()
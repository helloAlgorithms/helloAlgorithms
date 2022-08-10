import sys

def solution(nbr_list : list, case_list : list, nbr_list_len : int, case_list_len : int) -> list:
    dp_list = []
    for i in range(nbr_list_len):
        dp_list.append(nbr_list[i] + dp_list[i-1] if i > 0 else nbr_list[i])
    answer_list = []
    for i in range(case_list_len):
        if case_list[i][0] == case_list[i][1]:
            answer_list.append(nbr_list[case_list[i][1]-1])
        else:
            end = dp_list[case_list[i][1] - 1]
            start = dp_list[case_list[i][0] - 2] if case_list[i][0] > 1 else 0
            answer_list.append(end - start)
    return answer_list

def case_list_init(case_cnt : int) -> list:
    case_list = []
    for i in range(case_cnt):
        case_list.append(list(map(int, sys.stdin.readline().split())))
    return case_list

def print_answer_list(answer_list : list) -> None :
    for answer in answer_list: print(answer)

def runtime() -> None:
    nbr_list_len, case_list_len = map(int, sys.stdin.readline().split())
    nbr_list = list(map(int, sys.stdin.readline().split()))
    case_list = case_list_init(case_list_len)
    print_answer_list(solution(nbr_list, case_list, nbr_list_len, case_list_len))

runtime()

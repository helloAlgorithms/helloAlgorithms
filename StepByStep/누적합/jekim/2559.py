import sys

# def logger(degree_list : list, degree_list_len : int, day_cnt : int) -> None:
#     print(degree_list, degree_list_len, day_cnt)

def solution(degree_list : list, degree_list_len : int, day_cnt : int):
    part_sum = sum(degree_list[:day_cnt])
    answer = [part_sum]
    for i in range(0, len(degree_list) - day_cnt):
        part_sum = part_sum - degree_list[i] + degree_list[i + day_cnt]
        answer.append(part_sum)
    # logger(degree_list, degree_list_len, day_cnt)
    return max(answer)

def runtime() -> None:
    degree_list_len, day_cnt = map(int, sys.stdin.readline().split())
    degree_list = list(map(int, sys.stdin.readline().split()))
    print(solution(degree_list, degree_list_len, day_cnt))

runtime()
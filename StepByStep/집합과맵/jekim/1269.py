
# timeout
# def solution(a_list, b_list, a_list_len, b_list_len):
#     set_1 = []
#     set_2 = []
#     for i in range(a_list_len):
#         if a_list[i] not in b_list:
#             set_1.append(a_list[i])
#     for i in range(b_list_len):
#         if b_list[i] not in a_list:
#             set_2.append(b_list[i])
#     answer = len(set_1 + set_2)
#     print(answer)

def solution(a_list, b_list, a_list_len, b_list_len):
    elem_dict = {}
    for i in range(a_list_len):
        if a_list[i] not in elem_dict.keys(): elem_dict[a_list[i]] = 1
        else: elem_dict[a_list[i]] += 1
    for i in range(b_list_len):
        if b_list[i] not in elem_dict.keys(): elem_dict[b_list[i]] = 1
        else: elem_dict[b_list[i]] += 1
    set_1 = []
    set_2 = []
    for i in range(a_list_len): if elem_dict[a_list[i]] == 1: set_1.append(a_list[i])
    for i in range(b_list_len): if elem_dict[b_list[i]] == 1: set_2.append(b_list[i])
    answer = len(set_1 + set_2)
    return answer

def runtime():
    a_list_len , b_list_len = list(map(int, input().split()))
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    print(solution(a_list, b_list, a_list_len, b_list_len))

runtime()
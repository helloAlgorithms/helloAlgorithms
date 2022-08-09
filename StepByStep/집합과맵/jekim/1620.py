def solution(monster_list : list, query_list : list, input_cnt : int, query_cnt : int) -> list:
    monster_dict = { monster_list[i] : i + 1 for i in range(len(monster_list)) }
    answer_list = []
    for query in query_list:
        if query.isnumeric() == False: # name
            answer_list.append(monster_dict[query])
        else: # number
            answer_list.append(monster_list[int(query) - 1])
    return answer_list

def init_list(list_length : int) -> list: return [ input() for i in range(list_length) ]

def print_answer_list(answer_list : list) -> None :
    for answer in answer_list: print(answer)

def runtime(NoneType) -> None :
    input_cnt, query_cnt = map(int, input().split())
    monster_list = init_list(input_cnt)
    query_list = init_list(query_cnt)
    print_answer_list(solution(monster_list, query_list, input_cnt, query_cnt))

runtime()
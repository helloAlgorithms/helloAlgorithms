import sys
input = sys.stdin.readline

def is_pair_appeard(popped : str, string: str, opener_list : list, closer_list : list) -> bool:
    for i in range(len(opener_list)):
        if string == closer_list[i] and popped == opener_list[i]:
            return True
    return False

def is_paired(string: str, opener : list, closer : list) -> bool:
    length = len(string)
    for i in range(len(opener)):
        if string.count(opener[i], 0, length) != string.count(closer[i], 0, length): return False
    return True

def is_closed(string : str) -> bool:
    opener_list = ['(', '[']
    closer_list = [')', ']']
    stack = []
    if is_paired(string, opener_list, closer_list) == False: return False
    i = 0
    while i < len(string):
        if string[i] in opener_list:
            stack.append(string[i])
        elif string[i] in closer_list:
            if len(stack) == 0: return False
            if is_pair_appeard(stack[-1], string[i], opener_list, closer_list) == False: return False
            stack.pop(-1)
        i += 1
    return True if len(stack) % 2 == 0 else False 

def solution(input_list : list) -> list:
    return [ "yes" if is_closed(i) == True else "no" for i in input_list ]

def print_answer_list(answers : list) -> None:
    for i in answers: print(i)

def runtime() -> None:
    input_str_list = []
    while True:
        input_str_list.append(input().rstrip())
        if (len(input_str_list[-1]) == 1 and
            input_str_list[-1][0] == "."):
            input_str_list.pop()
            break
    print_answer_list(solution(input_str_list))

if __name__ == "__main__": runtime()
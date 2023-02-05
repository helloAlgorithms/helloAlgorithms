def solution(my_str, n):
    answer = []
    while my_str:
        answer.append(my_str[0:n])
        my_str = my_str[n:]
    return answer

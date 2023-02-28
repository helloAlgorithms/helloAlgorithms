def solution(array):
    answer = 0
    for a in array:
        answer+= str(a).count('7')
    return answer

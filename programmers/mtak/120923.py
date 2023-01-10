def solution(num, total):
    answer = [0 for i in range(num)]
    num_sum = num * (num + 1) / 2
    sparse = (total - num_sum) / num
    for i in range(num):
        answer[i] = i + 1 + sparse
    return answer

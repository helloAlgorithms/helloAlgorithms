def solution(numbers):
    answer = []
    for i, p in enumerate(numbers):
        t = list(filter(lambda x:x > p, numbers[i + 1:]))
        if len(t) == 0:
            answer.append(-1)
            continue
        answer.append(t.pop(0))
    return answer

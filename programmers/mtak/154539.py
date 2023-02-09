def solution(numbers):
    answer = [0] * len(numbers)
    for i, p in enumerate(numbers):
        t = -1
        for x in numbers[i + 1:]:
            if x > p:
                t = x
                break
        answer[i] = t
    return answer

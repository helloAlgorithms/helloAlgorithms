def solution(n):
    steps = [0 for _ in range(2001)]
    steps[1] = 1
    steps[2] = 2

    for i in range(3, 2001):
        steps[i] = (steps[i-1] + steps[i-2]) % 1234567

    return steps[n]

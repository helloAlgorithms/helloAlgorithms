import math
K,N = map(int, input().split(' '))
strings = [int(input()) for _ in range(K)]

def checkAvail(strings, base, goal):
    avail = 0;
    for length in strings:
        avail += math.trunc(length / base)
        if avail >= goal:
            return True
    return False

def solution(strings):
    minlen = 1
    maxlen = max(strings)
    answer = 0
    while (minlen <= maxlen):
        mid = int((minlen + maxlen) / 2)
        if checkAvail(strings, mid, N):
            minlen = mid + 1
            if (answer < mid): answer = mid
        else:
            maxlen = mid - 1
    return answer

print(solution(strings))

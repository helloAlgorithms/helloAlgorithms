import sys
N, M = map(int, input().split())
trees = list(map(int, sys.stdin.readline().strip().split()))

def checkAvail(trees, base, goal):
    avail = 0;
    for length in trees:
        if (length - base > 0):
            avail += length - base
        if avail >= goal:
            return True
    return False

def solution(trees):
    minlen = 1
    maxlen = max(trees)
    answer = 0
    while (minlen <= maxlen):
        mid = int((minlen + maxlen) / 2)
        if checkAvail(trees, mid, M):
            minlen = mid + 1
            if (answer < mid): answer = mid
        else:
            maxlen = mid - 1
    return answer
print(solution(trees))

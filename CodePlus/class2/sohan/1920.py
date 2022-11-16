N = int(input())
An = input().split(' ')
M = int(input())
Bn = input().split(' ')
An.sort()

def solution(number):
    first = 0
    end = N - 1

    while first <= end:
        mid = (first + end) // 2
        if An[mid] == number:
            return True
        if number < An[mid]:
            end = mid - 1
        elif number > An[mid]:
            first = mid + 1

for i in range(M):
    if (solution(Bn[i])):
        print(1)
    else:
        print(0)

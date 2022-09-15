# 11시06분 시작 11시 35분  
# 오타문제였는데 if in 문법을 모르고 틀린줄 알고
# 시간을 많이씀 

import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int,input().split()))
m = int(input())
li_my = list(map(int,input().split()))
li.sort()
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
for i in range(m):
    if binary_search(li, li_my[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')

# 시간 초과 소스
# import sys
# input = sys.stdin.readline

# n = int(input())
# li = list(map(int,input().split()))
# m = int(input())
# li_my = list(map(int,input().split()))

# li.sort()
# li_my.sort()

# for i in range(len(li_my)):
#     if li_my[i] in li:
#         li_my[i] = 1
#     else:
#         li_my[i] = 0
# for i in range(len(li_my)):
#     print(li_my[i],end=' ')
      

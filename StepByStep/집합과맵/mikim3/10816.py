# 08:53시작 09:42 끝
# 답봄

# 처음에 그냥 구현하고 당연히 시간초과가 뜨고 
# 이진탐색으로 바꾸면 그냥 단순히 해결될꺼라고 생각했는데 내장함수를 쓰는 방법 말고는
# 거의 안 됐다. 된다고 해도 시간이 너무 오래걸렸다.

# Counter라는 것이  있는지 몰랐고 그것이 시간 복잡도를 줄여줄지 몰랐다.
# 

# 내가 문제를 봤을때 가장 떠올릴 만한 것은 딕셔너리를 이용한 방법이였다.

n = int(input())
mycard = list(map(int,input().split()))
m = int(input())
question = list(map(int,input().split()))

dic_count = {}

for card in mycard:
    if card in dic_count:
        dic_count[card] += 1
    else:
        dic_count[card] = 1
for target in question:
    result = dic_count.get(target)
    if result == None:
        print(0, end = " ")
    else:
        print(result, end = " ")




####### Counter 이용
# from collections import Counter
# import sys
# input = sys.stdin.readline

# n = int(input())
# mycard = list(map(int,input().split()))
# m = int(input())
# question = list(map(int,input().split()))

# count = Counter(mycard)

# for i in range(len(question)):
#     if question[i] in count:
#         print(count[question[i]], end=' ')
#     else:
#         print(0, end = ' ')

# 시간 초과
# import sys
# input = sys.stdin.readline

# n = int(input())
# mycard = list(map(int,input().split()))
# mycard.sort()
# m = int(input())
# question = list(map(int,input().split()))

# def binary_search(array,target,start,end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return array[start:end + 1].count(target)
#     elif array[mid] < target:
#         return binary_search(array, target, mid+1, end)
#     else:
#         return binary_search(array, target, start, mid-1)

# for i in range(len(question)):
#     a = binary_search(mycard, question[i], 0, len(mycard)-1)
#     if a is not None:
#         print(a, end = ' ')
#     else:
#         print(0, end=' ')
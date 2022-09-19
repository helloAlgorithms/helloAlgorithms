# 22:33 시작 23:00 끝

# 키 포인트
# 사실 문제를 보자마자 그냥 배열 for 문은 시간초과라고 이제는 예측했다. "N, M은 500,000 이하의 자연수이다." 이라는 조건 때문이다.
# 그래도 일단 구현해보았고 역시나 안돼서 딕셔너리를 사용해보았다.

# 일단  배열 +  for 문으로 해본다. 속도문제로 안되면  딕셔너리를 사용해본다.
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
dic = {}

for i in range(n):
    dic[input().strip()] = 0
li_see = []
check_num = 0
li_check = []
for j in range(m):
    li_see.append(input().strip())
    if li_see[j] in dic:
        li_check.append(li_see[j])
li_check.sort()
print(len(li_check))
for i in range(len(li_check)):
    print(li_check[i])

# 시간초과 소스
# import sys
# input = sys.stdin.readline

# n, m = map(int,input().split())
# li_listen = []
# li_see = []

# for i in range(n):
#     li_listen.append(input().strip())
# for i in range(m):
#     li_see.append(input().strip())

# li_check = []
# for i in range(n):
#     for j in range(m):
#         if li_listen[i] == li_see[j]:
#             li_check.append(li_listen[i])

# print(len(li_check))
# li_check.sort()
# for i in range(len(li_check)):
#     print(li_check[i])








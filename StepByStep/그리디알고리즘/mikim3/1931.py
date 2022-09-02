
# 틀린 이유
# 2차원 배열안에 li[i][1] 처럼 2번째 항을 기준으로 정렬하는 방법을 몰랐다.

# li.sort(key = lambda x:x[0]) 를 하기 전에는
# 3    1 3 8 8 4 8 이 입력됐을때 출력  값이 2였다.  
# 하지만 추가 이후 제대로 나왔다.
# 키포인트
# 끝나는 시간이 빨리 끝나야 많은 강의를 들을수 있다.
import sys
input = sys.stdin.readline
n = int(input())
# 2차원 배열에서 2번째 항을 기준으로 정렬
li = []
for i in range(n):
    li.append(list(map(int,input().split())))
# x[1]기준으로 정렬 
li.sort(key = lambda x:x[0])
li.sort(key = lambda x:x[1])
now_time = 0
check = 0
for i in range(n):
    if li[i][0] >= now_time:
        check += 1
        now_time = li[i][1]
print(check)


# 시작시간 1807  
# 답봄
# 무슨소리를 하는지 못 알아 먹겠다.

# 3의 배수중 1로만 이루어진 가장 작은수는 111이다.  그래서 출력해야할 수는 111의 자리수 3이다.

# 가장 직관적인 코드
while True:
    try:
        x = int(input())
    except EOFError:
        break
    if x == 1:
        print('1')
        continue
    num = 1
    cnt = 1
    while True:
        num = num * 10 + 1
        cnt += 1
        if (num % x) == 0:
            print(cnt)
            break

# def solution(n):
#     count = 1
#     div = 1
#     while True:
#         if count == 1 : left = div%n
#         else : left = ((div%n)*(10%n)+1)%n
        
#         if left == 0 : return count
#         else :
#             div = left
#             count += 1

# while True :
#   try :
#     n = int(input())
#     print(solution(n))
#   except :
#     break

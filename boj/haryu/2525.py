# https://www.acmicpc.net/problem/2525


# 내가 진행한 방식
# import sys

# arr1 = list(map(int, sys.stdin.readline().rstrip().split()))
# timer = int(sys.stdin.readline().rstrip())

# hour = 0
# temp_minute = arr1[1] + timer
# while temp_minute > 60 :
#   hour += 1
#   temp_minute -= 60
# if temp_minute == 60 :
#   temp_minute = 0
#   hour += 1
# arr1[0] += hour
# if arr1[0] >= 24 :
#   arr1[0] %= 24 
# arr1[1] = temp_minute
# print(arr1[0], arr1[1])

# 극한의 최적화 방식(백준 1등)
# A,B=map(int,input().split())
# C=int(input())
# print((A+((B+C)//60))%24,(B+C)%60)
# // 정수형으로 나눌 때 사용 하는 연산자 

# 좀더 최적화하면 다음과 같이 구현 가능하다. 
import sys 

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline().strip())
M = B + C
print(((A + (M // 60)) % 24), M % 60)

# 알아둘 사항 input()의 경우 자동적으로 값을 정리해서 최적화 해주는 역할까지 한다. 따라서 느리다. 
# 이 말은 str이 그대로 필요할 때 조금이라도 속도를 향상시키고자 다른 작업들을 뺀 sys.stdin.readline() 을 쓰는 방법도 고려된다. 
# 하지만 지금처럼 int 형변환이 필요한 경우 굳이 sys 쓸 이유는 없고, input을 쓰면 된다. 
# 그런 점에서 readline의 경우 뒤에 개행문자를 포함해서 여러 쓸데 없는 값을 가지고 있고, 
# 그렇기에 int 형변환이 정상적으로 되지 않는다. 
# 따라서 TypeError 가 발생했던 것이기에 sys.stdin.readline()을 할경우 split을 하거나 strip 메서드를 통해 개행문자 등을 제거해줘야 한다. 
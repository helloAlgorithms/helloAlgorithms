######### 10단계 재귀방식 시작

# 10872 번 문제
# 팩토리얼
# 입력
# 재귀함수로 풀어보자 
#N!
n=int(input())

def factorial(m):
    if m==0:
        return 1
    return m*factorial(m-1) 

print(factorial(n))
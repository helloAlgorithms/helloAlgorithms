# 
# 일단 문제의 이해가 어려웠다.
# 과정도 여러가지 과정이 필요해서 시간이 좀더 걸렸다.

# 17 8
# 2
# 2 16

# 주어진 A진법 표현할 B진법
# A는 2개의 수로 이루어져있다.
# 두번째 자리수는 2 첫번째 자리수는 16이다.

A_zin, B_zin = map(int, input().split())
m = int(input())
A = list(map(int, input().split()))

# A를 10진법으로 변환
A_10 = 0
A.reverse()
for i in range(len(A)):
    A_10 += A[i]*(A_zin ** (i)) 
# print(A_10)
# A의 10진법 값을 B진법으로 변환
B_su = []
while (A_10 >= B_zin):
    B_su.append(A_10 % B_zin)
    A_10 = A_10//B_zin 
B_su.append(A_10%B_zin)

B_su.reverse()
for i in range(len(B_su)):
    print(B_su[i],end=' ')


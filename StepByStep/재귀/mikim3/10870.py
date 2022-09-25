# 10870 번 문제 
# 피보나치 수 5
# n이 1이면 0, 1 까지 출력 답이 1이됨 

n=int(input())

def pivonachi(m):
    if m==2:
        return 1
    elif m==0:
        return 0
    elif m==1:
        return 1
    else:
        return pivonachi(m-2)+pivonachi(m-1)

print(pivonachi(n))

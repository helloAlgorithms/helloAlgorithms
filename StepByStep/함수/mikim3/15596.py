
def solve(a):   #  a는 리스트
    
    n=len(a)  # 
    su=0
    for i in range(n):
        su+=a[i]
    
    return  su # a 에 포함되어 있는 정수 n개의 합(정수)
print(solve([1,2,3,4,5]))
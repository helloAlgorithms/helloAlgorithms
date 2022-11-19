a=int(input())
b=int(input())
c=int(input())
d= a*b*c
st=str(d)

arr=[0 for i in range(10)]
for i in range(10):  # 각 숫자 마다 반복
    for j in range(len(st)):  # 계산된 값 숫자마다 반복
        if int(st[j])==int(i):  # 
            arr[i]+=1
for i in range(10):
    print(arr[i])
            
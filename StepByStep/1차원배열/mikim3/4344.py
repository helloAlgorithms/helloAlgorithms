
n = int(input())
sum=0
avg = 0
avgup=0
avgarr=[]
for i in range(n):
    arr = list(map(int,input().split()))  #  5 50 50 70 80 100
    sum=0 # 점수합
    avgup=0
    for j in range(arr[0]): # 한 반에 인원수
        sum+=arr[j+1] # 1번인덱스부터 총합에 더한다
    avg=sum/(arr[0])  # 총합/인원수 는 평균
    
    for x in range(arr[0]):
        if  arr[x+1]-avg>0:
            avgup+=1    #평균보다 높은사람 +1
    # avgarr[i]=round(avgup/n,3)
    avgarr.append(round(avgup/arr[0]*100,3))
    avgarr[i]=round(avgup/arr[0]*100,3)
    
for i in range(n):
    print("{:.3f}%".format(avgarr[i],end='%\n'))  # format 함수는 몰랐네
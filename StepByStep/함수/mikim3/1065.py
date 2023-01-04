# 정수 X의 각 자리가 등차수열을 이루면 그 수를 한수라고 한다.
# 두자리수는 다 한수다
# 세자리부터 비교하면 된다
n=int(input())  # 알아야할 한수의 범위를 알려줄 수
num=0 
for i in range(1,n+1):
    nArray=list(map(int,str(i)))   # 그 수의 각자리를 비교하기 위해 각자리를 분리
    if i < 100:
        num+=1  # 한수 맞으니 카운트
    elif nArray[0]-nArray[1]==nArray[1]-nArray[2]:
        num+=1
print(num)
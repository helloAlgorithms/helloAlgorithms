n = int(input())  # 시도할 횟수
arr=[] #한번 반복마다 바뀔 배열
sum =0 # 점수 0 부터시작
contin=0# 연승확인
sumarr=[] # 연승리스트
for i in range(n): # 전체 시도할 횟수 반복
    arr=input() # 초기화 겸 입력
    sum=0
    contin=0
    for j in range(len(arr)): # OX갯수 만큼 반복
        if arr[j]=='O': # O일 경우
            contin+=1 # 연승점수 +1  
            sum+=contin  # 연승점수를 총합에 더함
        if arr[j]=='X':#X일경우
            contin=0
    sumarr.append(sum)
    
for i in range(n):
    print(sumarr[i])
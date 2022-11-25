# 1316 번 문제 
# 그룹 단어 체커
# 문자열 다루는 기술이 부족해서 문법찾아봄

# 이 문법 꼭 잘쓰기 if in 
# if word[j] in arr:   # word[j] 가 arr안에 있다면 

n = int(input())   # 받을 문자열 갯수
count=0  # 그룹 단어 갯수 
arr=[]  # 

for i in range(n):   # n번 반복하여 받기
    now='1'  # 현재 그룹되는 문자
    word=input()  # 문자열 받기 현재 분석할 단어  
    #  조건 1 직전 인덱스에 문자와 같다면 넘어간다
    #  조건 2 직전 인덱스에 문자와 다르다면 지금까지 쭉 나온 인덱스와 비교해본다 만약 같은게 있다면 count하지말고 이번 단어를 넘긴다.
    #  만약 같은게 없다면 다시 다음 문자로 넘어간다.
    for j in range(len(word)):
        if  now==word[j]:
            arr.append(word[j])
            pass
        else:
            if word[j] in arr:   # word[j] 가 arr안에 있다면 
                count-=1
                break
        arr.append(word[j]) # 
        now=word[j]
    count+=1 
    arr.clear()  # 
print(count)

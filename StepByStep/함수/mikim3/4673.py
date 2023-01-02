# 처음에 문제를 제대로 안봐서 애먹었음
def solve(n):  # solve(75) = 75 + 7 + 5 = 87
    m=0
    nstr=str(n)  # 자리수를 인덱스로 나눈다
    if len(nstr)==1:  # 한자리수
       m=n+n 
    elif len(nstr)==2:  # 두자리수
       m=n+int(nstr[0])+int(nstr[1]) 
    elif len(nstr)==3:  # 세자리수
       m=n+int(nstr[0])+int(nstr[1])+int(nstr[2])
    elif len(nstr)==4:  # 네자리수
       m=n+int(nstr[0])+int(nstr[1])+int(nstr[2])+int(nstr[3])
    return m
# 문제에서 요구하는 것은 생성자 즉 solve로 값이 한번이라도 나오는 값은 뺴고 나머지를 출력해야함
# 즉 차집합을 구하자
# s1- s2 또는 s1.difference(s2)  이런식으로 표현가능
s=set(i for i in range(10001))
for i in range(1,10001):
    s.discard(solve(i))  # 집합에 생성자가 한번이라도 포함되면 제거
for i in range(1,10001):
    if i in s:
        print(i)
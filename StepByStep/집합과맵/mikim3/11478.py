# 11:10 시작  11:22 끝

# ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc가 있고, 서로 다른것의 개수는 12개이다.

# 부분 문자열을 만든후 중복은 dict를 이용해서 처리할 수 있다.

li = input()

# 만든 글자를 임시로 저장
st = ""
# dic 
dic = {}
# 
total = 0
for i in range(len(li)): # 글자의 길이 경우의 수 만큼 반복한다.
    for j in range(len(li) - i):  # 앞에 글자부터 한글자씩 만든다
        st += li[j:j+i+1]
        total += 1
        if st in dic:
            dic[st] += 1
        else:
            dic[st] = 0
        st=""
    
print(total - sum(dic.values()))



# 1105시작  1131끝   
# 답봄
# 딕셔너리에 대한 이해가 부족했고 li.index()를 이용하면 시간효율성이 매우 떨어진다는 것을
# 몰랐다.

import sys
input = sys.stdin.readline
n , m = map(int,input().split())
dic = {}
for i in range(1, n + 1):
    a = input().rstrip()
    # 해당인덱스 키에 포켓몬이름 벨류
    dic[i] = a
    # 포켓몬 이름 키에 인덱스 번호 벨류
    dic[a] = i
for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dic[int(quest)])
    else:
        print(dic[quest])



# 시간초과소스
# import sys
# input = sys.stdin.readline
# n , m = map(int,input().split())
# li_poke = []
# for i in range(n):
#     li_poke.append(input().strip())
# li_qus = []
# for i in range(m):
#     li_qus.append(input().strip())
    
# for i in range(m):
#     if li_qus[i].isdigit():
#         print(li_poke[int(li_qus[i])-1])
#     elif li_qus[i].isalpha():
#         print(li_poke.index(li_qus[i])+1)
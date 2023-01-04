# 2675 번
# 문자열 반복
t = int(input())
for i in range(t):
    a,b=list(map(str,input().split()))  #
    for z in range(len(b)):  # 글자수 만큼 반복
        for j in range(int(a)):  # 입력받은 값 만큼 반복
            print(b[z],end='')
    print("")
    
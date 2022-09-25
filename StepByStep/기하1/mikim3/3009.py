# 시작시간 06:19  풀은 시간 06:29
# 답지봄

# 먼저 임시변수 x,y 에 넣은 이후 배열에 다시 넣는 방법을 생각해내지 못했다.

x_s = []
y_s = []

for i in range(3):
    x, y = map(int,input().split())
    x_s.append(x)
    y_s.append(y)

for i in range(3):
    count = 0
    for j in range(3):
        if x_s[i] == x_s[j]:
            count+=1
    if count == 1:
        print(x_s[i],end=' ')
    

for i in range(3):
    count = 0
    for j in range(3):
        if y_s[i] == y_s[j]:
            count+=1
    if count == 1:
        print(y_s[i],end='')
    

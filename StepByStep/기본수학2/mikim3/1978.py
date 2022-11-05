import sys
input = sys.stdin.readline


n = int(input())
li = list(map(int,input().split()))
count = 0
flag = 0 

for i in range(n):
    if li[i] == 1:
        flag = 1
    for j in range(2,li[i]//2+1):
        if li[i] % j == 0:
            flag += 1
            break
    if flag < 1:
        # print(li[i])
        count+=1
    flag = 0
print(count)





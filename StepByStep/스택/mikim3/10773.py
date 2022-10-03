# 0822 시작 0825 끝

li = []
k = int(input())

for i in range(k):
    temp = int(input())
    if temp != 0:
        li.append(temp)
    else:
        li.pop()
        
print(sum(li))

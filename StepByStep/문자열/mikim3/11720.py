# 11720 번
# 숫자의 합

n = int(input())
a = int(input())
sum=0

for i in range(len(str(a))):
    sum+=int(str(a)[i])
print(sum)

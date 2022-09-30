# 시작시간 11:51 종료시간 12:03

n = int(input())

if n == 1:
    exit(0);

count = 0
i = 2
while (n != i):
    if n % i == 0:
        n //= i
        print(i)
        i = 1
        # print("n == ",n)
    i += 1
print(n)
    

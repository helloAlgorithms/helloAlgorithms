import sys
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
min = -1
sum = 0
for i in range(m, n + 1):
    if i == 2:
        min = 2
        sum += 2
    for j in range(2, i):
        if i % j == 0:
            break
        if j == i - 1:
            if min == -1:
                min = i
            sum += i

if min == -1 :
    print(min)
else:
    print(sum)
    print(min)

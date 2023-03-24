import sys

N = int(input())

sqrt_n = N ** 0.5

if sqrt_n.is_integer():
     print('1')
     exit(0)

for i in range(1, int(sqrt_n) + 1):
    tmp = N - i**2
    if (tmp ** 0.5).is_integer():
        print('2')
        exit(0)

for i in range(1, int(sqrt_n) + 1):
    for j in range(1, int((N - i**2) ** 0.5) + 1):
        if ((N - i**2 - j**2) ** 0.5).is_integer():
            print('3')
            exit(0)

print('4')
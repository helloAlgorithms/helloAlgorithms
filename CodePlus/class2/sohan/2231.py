N = input()
digit = len(N)
num = 10 ** (digit - 1) - 1
N = int(N)

def partial_sum(num):
    res = 0
    while num:
        res = res + (num % 10)
        num = num // 10
    return (res)

while num + partial_sum(num) != N:
    num = num + 1
    if num == N:
        print(0)
        exit(0)
print(num)

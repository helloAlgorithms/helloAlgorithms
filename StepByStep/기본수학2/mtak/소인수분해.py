import sys
def func(n, d):
    if n == 1:
        return 
    elif n % d != 0:
        func(n,d + 1)
    else:
        print(d)
        func(n//d, d)

#sys.setrecursionlimit(10000)
#func(int(sys.stdin.readline()), 2)

d = 2
n = int(sys.stdin.readline())
while n != 1:
    if n % d != 0:
        d+=1
        continue
    print(d)
    n //= d


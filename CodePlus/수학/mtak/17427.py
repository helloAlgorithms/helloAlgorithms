import sys
input = sys.stdin.readline
def f(y):
    l = []
    for i in range(1, int(y **(1/2)) + 1):
        if y % i == 0:
            l.append(i)
            if i ** 2 != y:
                l.append(y//i)
    return sum(l)
def g(x):
    sum = 0
    for i in range(1, x + 1):
        sum += f(i)
    return sum

n = int(input())
print(g(n))


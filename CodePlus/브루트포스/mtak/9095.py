import sys
input = sys.stdin.readline
case = int(input())
def f(i):
    if i == 1:
        return 1
    elif i == 2:
        return 2
    elif i == 3:
        return 4
    else:
        return f(i - 1) + f(i - 2) + f (i - 3)
for _ in range(case):
    c = int(input())
    print(f(c))
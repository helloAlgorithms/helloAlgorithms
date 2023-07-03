import sys

def solve(x):
    if x <= 1:
        print(1)
    elif x % 2 == 1:
        print((pow(4,(x + 1) // 2) - 1) // 3)
    else:
        print((2 * pow(2,x) + 1) // 3)

for line in sys.stdin:
    solve(int(line))

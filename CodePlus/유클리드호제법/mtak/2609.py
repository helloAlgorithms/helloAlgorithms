import sys
input = sys.stdin.readline
x, y = map(int, input().split())

def getGCD(x, y):

    while y != 0:
        y, x = x % y, y
    return x

def getLCM(x, y):
    return x * y // getGCD(x, y)

print(getGCD(x, y))
print(getLCM(x, y))


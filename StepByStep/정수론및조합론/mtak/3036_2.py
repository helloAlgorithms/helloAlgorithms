import sys
input = sys.stdin.readline

cnt = int(input())
rl = list(map(int, input().split()))

def getGCD(a, b):
    while b!= 0:
        a, b = b, a%b
    return a

for i in rl[1:]:
    div = getGCD(i, rl[0])
    print("%d/%d"%(rl[0]/div, i/div))
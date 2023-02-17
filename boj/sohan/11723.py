import sys

M = int(input())
S = 0

for _ in range(M):
    o = sys.stdin.readline().split()
    if o[0] == "add":
        S |= (1 << int(o[1]))
    elif o[0] == "remove":
        S &= ~(1 << int(o[1]))
    elif o[0] ==  "check":
        print(1 if S & (1 << int(o[1])) else 0)
    elif o[0] == "toggle":
        S ^= (1 << int(o[1]))
    elif o[0] == "all":
        S = (2 ** 21) - 1
    else:
        S = 0
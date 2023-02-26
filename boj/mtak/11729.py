import sys
input = sys.stdin.readline
x = int(input())
#sys.setrecursionlimit(10**7)
ret = []
def hanoi(s, m, e, n):
    if n == 1:
        ret.append([s, e])
        return 
    hanoi(s, e, m, n - 1)
    hanoi(s, m, e, 1) 
    hanoi(m, s, e, n - 1)
hanoi(1, 2, 3, x)
print(len(ret))
for _ in ret:
    print(_[0], _[1])

import sys
input = sys.stdin.readline
x, y = map(int, input().split())
A = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
M = ['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
s = 0
for _x in range(x - 1):
    s += A[_x]
s += y
print(M[s % 7])


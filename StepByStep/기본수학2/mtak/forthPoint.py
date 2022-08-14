import sys

def func(a, b, c):
    if a == b:
        return c
    elif a == c:
        return b
    else:
        return a

_coordinates = list()
for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    _coordinates.append([x, y])
print(func(_coordinates[0][0], _coordinates[1][0], _coordinates[2][0]), func(_coordinates[0][1], _coordinates[1][1], _coordinates[2][1]))
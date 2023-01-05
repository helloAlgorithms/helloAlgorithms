import sys

N, M = map(int, input().split())
deud = {sys.stdin.readline() for _ in range(N)}
bo = {sys.stdin.readline() for _ in range(M)}
deudbo = sorted(deud & bo)

print(len(deudbo))
print(''.join(deudbo), end='')

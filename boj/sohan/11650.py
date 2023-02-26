import sys
N = int(input())
pairs = [list(map(int, sys.stdin.readline().strip().split(' '))) for i in range(N)]
pairs = sorted(pairs, key=lambda x: (x[1], x[0]))
for pair in pairs:
    print(*pair, sep=' ')

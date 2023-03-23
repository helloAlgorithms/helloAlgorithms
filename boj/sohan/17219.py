import sys

N, M = map(int, input().split(' '))

db = dict()

for _ in range(N):
    site, pw = sys.stdin.readline().strip().split(' ')
    db[site] = pw

for _ in range(M):
    print(db[sys.stdin.readline().strip()])
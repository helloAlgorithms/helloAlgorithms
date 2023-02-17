import sys

N, M = map(int, input().split())
dogam = {_:sys.stdin.readline().strip() for _ in range(1, N + 1)}
rdogam = {v:k for k,v in dogam.items()}
ans = ""

for _ in range(M):
    a = sys.stdin.readline().strip()
    if a[0].isdigit() == 1:
        ans += dogam[int(a)] + '\n'
    else:
        ans += str(rdogam[a]) + '\n'
print(ans, end='')

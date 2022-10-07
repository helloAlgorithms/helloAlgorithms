N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split())) for i in range(N)]
C = [list(c + d for c, d in zip(a, b)) for a, b in zip(A, B)]
for element in C:
    print(' '.join(map(str, element)))

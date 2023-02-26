T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    k = x
    while  k <= M * N:
        if (k - x) % M == 0 and (k - y) % N == 0:
            break
        k += M
    
    print(k if k <= M * N else "-1")
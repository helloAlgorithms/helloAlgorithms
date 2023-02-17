T = int(input())
Ns = [int(input()) for _ in range(T)]

for N in Ns:
    F0 = 0
    F1 = 1
    Fn = 0
    for i in range(2, N + 1):
        Fn = F0 + F1
        F0 = F1
        F1 = Fn
    if N != 0:
        print(F0, F1, sep=' ')
    else:
        print(F1,F0, sep=' ')

def runtime() -> None:
    N = int(input())
    A = list(map(int, input().split()))
    V = int(input())
    print(A.count(V))

runtime()
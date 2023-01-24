from collections import deque

N, K = map(int, input().split())

def s():
    v = [0] * (10**5 + 1)
    d = deque()
    d.append([N, 0])
    v[N] = 1
    
    while len(d) != 0:
        X = d.popleft()
        v[X[0]] = 1
        if X[0] == K:
            break
        if X[0] - 1 >= 0 and v[X[0] - 1] == 0:
            v[X[0] - 1] == 1
            d.append([X[0] - 1, X[1] + 1])
        if X[0] + 1 <= 10**5 and v[X[0] + 1] == 0:
            v[X[0] + 1] == 1
            d.append([X[0] + 1, X[1] + 1])
        if (2 * X[0]) <= 10**5 and v[2 * X[0]] == 0:
            v[2 * X[0]] == 1
            d.append([2 * X[0], X[1] + 1])

    return X[1]

print(s())

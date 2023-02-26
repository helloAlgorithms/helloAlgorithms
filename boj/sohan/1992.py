N = int(input())
qd = [list(map(str, input())) for _ in range(N)]

def same(q):
    f = q[0][0]
    for i in q:
        for j in i:
            if f != j:
                return False
    return True

def rec(qd, N):
    step = N // 2
    for i in range(0, N, step):
        for j in range(0, N, step):
            q = [row[j:j + step] for row in qd[i:i + step]]
            if same(q) == False:
                print("(", end='')
                rec(q, N // 2)
            else:
                print(q[0][0], end='')
    print(")", end='')

if same(qd):
    print(qd[0][0])
else:
    print("(",end='')
    rec(qd, N)

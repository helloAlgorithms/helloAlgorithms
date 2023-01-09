N = int(input())
pp = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0]

def same(p):
    f = p[0][0]
    for i in p:
        for j in i:
            if f != j:
                return False
    return True

def r(p, N, ans):
    step = N // 2
    for i in range(0, N, step):
        for j in range(0, N, step):
            c = [r[j:j + step] for r in p[i:i + step]]
            if same(c) == False:
                ans = r(c, step, ans)
            else:
                ans[0] += int(c[0][0] == 0)
                ans[1] += int(c[0][0] == 1)
    return ans

if same(pp) == False:
    ans = r(pp, N, ans)
    print(ans[0])
    print(ans[1])

else:
    print("0\n1" if pp[0][0] == 1 else "1\n0")

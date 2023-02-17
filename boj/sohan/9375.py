N = int(input())

for i in range(N):
    d = {}
    ans = 1
    n = int(input())
    for j in range(n):
        n, c = input().split()
        try:
            if n not in d[c]:
                d[c].append(n)
        except:
            d[c] = [n]
    for n, c in d.items():
        ans = ans * (len(c) + 1)
    print(ans - 1)

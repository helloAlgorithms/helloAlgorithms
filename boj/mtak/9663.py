n = int(input())
col = [None] * n
tot = 0
def isValid(l):
    for i in range(l):
        if (col[i] == col[l] or abs(col[l] - col[i]) == l - i):
            return False
    return True
def nq(x):
    global tot
    if x == n:
        tot += 1
    else:
        for i in range(n):
            col[x] = i
            if (isValid(x)):
                nq(x + 1)
                
nq(0)
print(tot)


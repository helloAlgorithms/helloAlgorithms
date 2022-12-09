n = int(input())
s = input()

def get_table(p):
    tb = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j and p[i] != p[j]:
            j = tb[j - 1]
        if p[i] == p[j]:
            j += 1
            tb[i] = j
    return tb

tb = get_table(s)
print(n - tb[-1])
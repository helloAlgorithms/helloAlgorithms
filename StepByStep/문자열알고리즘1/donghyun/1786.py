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

def KMP(t, p):
    tb = get_table(p)
    result = []
    j = 0
    for i in range(len(t)):
        while j and t[i] != p[j]:
            j = tb[j - 1]
        if t[i] == p[j]:
            if j == len(p) - 1:
                result.append(i - len(p) + 2)
                j = tb[j]
            else:
                j += 1
    return result
text, pattern = input(), input()
idxs = KMP(text, pattern)
print(len(idxs))
print(*idxs)
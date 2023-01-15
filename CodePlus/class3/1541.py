eq = input()

ans = 0
minus = 1
n = ""

for c in eq:
    if c != '-' and c != '+':
        n += c
    else:
        ans += int(n) * minus
        n = ""
        if c == '-':
            minus = -1
ans += int(n) * minus
print(ans)

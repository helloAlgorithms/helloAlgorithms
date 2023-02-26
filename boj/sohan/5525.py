N = int(input())
M = int(input())
S = input()
i = 1
j, ans = 0,0

l = len(S)

while i <= l - 1:
    if S[i - 1] == 'I' and S[i] == 'O' and S[i + 1] == 'I':
        j += 1
        if j == N:
            j -= 1
            ans += 1
        i += 1
    else:
        j = 0
    i += 1

print(ans)
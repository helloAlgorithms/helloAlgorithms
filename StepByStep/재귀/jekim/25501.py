def recursion(s, l, r, ret):
    ret += 1
    if l >= r: return [1, ret]
    elif s[l] != s[r]: return [0, ret]
    else: return recursion(s, l+1, r-1, ret)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)

def runtime():
    inputs = []
    cnt = int(input())
    for i in range(cnt):
        inputs.append(input())
    for i in range(cnt):
        ans = isPalindrome(inputs[i])
        print(f"{ans[0]} {ans[1]}")
    
runtime()
import sys
sys.setrecursionlimit(100000)
n = int(input())
cases = [0] * (n + 1)
cases[1] = 1
cases[2] = 2 
def dfs(w):
    global cases
    if w < 3 or cases[w] > 0 :return cases[w]
    cases[w] = dfs(w - 1) + dfs(w - 2)
    return cases[w]
    
print(dfs(n)%10007)

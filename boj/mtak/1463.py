import sys
input = sys.stdin.readline
N = int(input())
memo = {1:0, 2:1}
def recurse(n):
    if n in memo:
        return memo[n]
    memo[n] = 1 + min(recurse(n//3) + n % 3, recurse(n // 2) + n % 2)
    return memo[n]
print(recurse)

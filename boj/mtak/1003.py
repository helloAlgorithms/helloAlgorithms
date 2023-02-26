t = int(input())
dp = [[1, 0], [0, 1]]
dp.extend([[] for _ in range(39)])
for _ in range(t):
    n = int(input())
    def fib(a):
        global dp
        if len(dp[a]) != 0: return dp[a]
        else:
            first = fib(a - 1)
            second = fib(a - 2)
            dp[a].append(first[0] + second[0])
            dp[a].append(first[1] + second[1])
            return dp[a]
    fib(n)
    print(dp[n][0], dp[n][1])

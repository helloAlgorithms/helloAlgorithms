import sys
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dp = [[0]*n for _ in range(n)]
for i in range(1,n):          
    for j in range(n-i):       
        x = i + j
        dp[j][x] = 2 ** 32
        # for d in dp:
        #     print(d, end="\n")
        for k in range(j,x):  
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + graph[j][0] * graph[k][1] * graph[x][1])
            # print("dp[j][k] == dp[%d][%d] %d dp[k+1][x] == dp[%d][%d] %d"%(j, k, dp[j][k] ,  k + 1, x, dp[k+1][x]))
            # print("graph[j][0] %d graph[k][1] %d graph[x][1] %d"%(graph[j][0] , graph[k][1] , graph[x][1]))
# for d in dp:
#     print(d, end="\n")
print(dp[0][n-1])
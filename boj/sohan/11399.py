N = int(input())
P = list(map(int, input().split()))
p = [0] * N

P.sort()

p[0] = P[0]

for i in range(1,N):
    p[i] = p[i - 1] + P[i]

print(sum(p))

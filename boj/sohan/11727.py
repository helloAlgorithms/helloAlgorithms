n = int(input())

d = [0] * (n + 1)

d[0] = 1
d[1] = 3

for i in range(2,n):
    d[i] = (2 * d[i - 2] + d[i - 1]) % 10007

print(d[n - 1])
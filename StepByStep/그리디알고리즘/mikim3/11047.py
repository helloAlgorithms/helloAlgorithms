
n, k = map(int, input().split())

li = []
for i in range(n):
    li.append(int(input()))
count = 0
for i in range(n-1,-1,-1):
    count = count + (k // li[i])
    k = k % li[i]
print(count)

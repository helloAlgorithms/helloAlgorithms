n1,n2,n3 = map(int,input().split())
total = 0
if n1 == n2 == n3:
    total = 10000 + n1*1000
elif n1 == n2 or n1 == n3:
    total = 1000 + n1 * 100
elif n2 == n3:
    total = 1000 + n2 * 100
else:
    total = max(n1,n2,n3) * 100
print(total)
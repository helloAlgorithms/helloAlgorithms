
a,b = list(map(int, input().split()))
c = int(input())

b += c

while b >= 60:
    if b >= 60:
        a += 1
        if a >= 24:
            a = 0
        b -= 60
print(a,b)

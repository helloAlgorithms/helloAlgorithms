N = int(input())
if N == 1:
    print(1)
    exit(0)
a = 1
An = 3*a**2 - 3*a + 1
while (An < N):
    a = a + 1
    An = 3*a**2 - 3*a + 1
print(a)

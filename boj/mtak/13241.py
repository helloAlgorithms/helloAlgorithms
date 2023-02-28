n, m = map(int, input().split())
def GCD(a, b):
    if b == 0:
        return a
    a, b = b, a%b
    return GCD(a, b)
print((n * m )// GCD(n, m))
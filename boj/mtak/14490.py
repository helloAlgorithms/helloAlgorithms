n, m = map(int, input().strip().split(":"))
def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a
_gcd = gcd(max(n, m), min(n, m))
print( f'{n//_gcd}:{m//_gcd}')
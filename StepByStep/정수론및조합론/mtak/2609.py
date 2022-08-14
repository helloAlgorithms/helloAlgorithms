import sys
 
input = sys.stdin.readline
 
def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a
 
if __name__ == "__main__":
    a, b = map(int, input().split())
    x, y = (b, a) if a > b else (a, b)
 
    gcd = GCD(x, y)
 
    lcm = a * b // gcd
 
    print(gcd)
    print(lcm)

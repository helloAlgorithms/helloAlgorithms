import math
x, y = map(int, input().split(' '))
print(math.gcd(x, y))
print((x * y) // math.gcd(x, y))

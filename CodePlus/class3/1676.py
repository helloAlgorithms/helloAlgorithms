import math

N = int(input())
f = str(math.factorial(N))

for i,c in enumerate(reversed(f)):
    if c != '0':
        print(i)
        break

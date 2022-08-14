import sys
import math
def isPrimary(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

_input = -1
while _input != 0:
    _input = int(sys.stdin.readline())
    if _input == 0:
        continue
    cnt = 0
    for i in range(_input +1, 2 * _input + 1):
        if isPrimary(i):
            cnt += 1
    print(cnt)

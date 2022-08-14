from re import I
import sys
import math

def isPrimary(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    if n == 1:
        return False
    return True

_cases = int(sys.stdin.readline())
while _cases:
    _cases-=1
    _i = int(sys.stdin.readline())
    _candidate = []
    _min_candidate = []
    for i in range(2, _i):
        if isPrimary(i):
            if isPrimary(_i - i) and _i >= 2 * i:
                _candidate.append(i)
                _min_candidate.append(_i - 2*i)
    a = _candidate[_min_candidate.index(min(_min_candidate))]
    print(a, _i - a)
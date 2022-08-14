import sys

def distance(_from, _to):
    return (_from[0] - _to[0])**2 + (_from[1] - _to[1]) ** 2

_testCase = int(sys.stdin.readline())
while _testCase:
    _testCase -= 1
    _input = list(map(int, sys.stdin.readline().split()))
    _flag = distance([_input[0], _input[1]], [_input[3], _input[4]])
    _flag1 = (_input[2] + _input[5]) ** 2
    _flag2 = (_input[2] - _input[5]) ** 2
    if _flag == 0 and _input[2] == _input[5]:
        print(-1)
    elif _flag == _flag1 or (_flag != 0 and _flag == _flag2):
        print(1)
    elif _flag > _flag1 or _flag < _flag2:
        print(0)
    else:
        print(2)

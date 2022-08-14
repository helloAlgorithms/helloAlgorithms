import sys
_cnt = int(sys.stdin.readline())
_input = list(map(int, sys.stdin.readline().split()))
for i in _input:
    if i == 1:
        _cnt -= 1
        continue
    for j in range(2, i):
        if i % j == 0:
            _cnt-=1
            break
print(_cnt)
    

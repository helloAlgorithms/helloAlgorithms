import sys

while True:
    _slide = list(map(int, sys.stdin.readline().split()))
    if sum(_slide) == 0:
        break
    _max = max(_slide)
    _slide.remove(max(_slide))
    if _max ** 2 == _slide[0] ** 2 + _slide[1] ** 2:
        print("right")
    else:
        print("wrong")
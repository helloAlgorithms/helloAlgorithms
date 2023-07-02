def solution(sides):
    sides.sort()
    return  2 if sides[-1] >= sum(sides[:-1]) else 1
def solution(firstLine, secondLine):
    n = firstLine
    path = list(secondLine.split())
    x, y = 1, 1
    direction = {"U":(0, -1), "D":(0, 1), "R":(1,0), "L":(-1,0)}
    for p in path:
        x, y = (x + direction[p][0]) % n, (y + direction[p][1]) % n
    return str(x) +" " + str(y)


def test_solution():
    assert solution(5, "R R R U D D")
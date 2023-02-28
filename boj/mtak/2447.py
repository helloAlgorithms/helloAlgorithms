import sys
input = sys.stdin.readline


def duplicate(f, n, Stars):
    _list = []
    for _ in range(3):
        for s in Stars:
            if f == 1:
                _list.append(s * 3)
                continue
            _list.append(s + ' ' * (n//3) + s)
        f = (0 if f == 1 else 1)
    return _list


def star(n):
    if n == 1:
        return ['*']
    Stars = star(n // 3)
    return duplicate(1, n, Stars)


print('\n'.join(star(int(input()))))

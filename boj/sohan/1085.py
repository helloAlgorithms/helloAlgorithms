x, y, w, h = map(int, input().split(' '))

def solution(x, y, w, h):
    answer = []
    answer.append(x)
    answer.append(y)
    answer.append(h - y)
    answer.append(w - x)
    return (sorted(answer)[0])

print(solution(x, y, w, h))

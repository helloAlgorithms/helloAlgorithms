N, r, c = list(map(int, (input().split())))

def solution(N, r, c):

    mid = (2 ** N) // 2
    square_count = 0
    square_index = 0

    while mid > 0:
        quadrant = [0,0]
        if r >= mid:
            quadrant[0] = 1
            r = r - mid
        if c >= mid:
            quadrant[1] = 1
            c = c - mid
        if quadrant == [0,0]:
            square_count = 0
        elif quadrant == [0,1]:
            square_count = 1
        elif quadrant == [1,0]:
            square_count = 2
        else:
            square_count = 3

        square_index += mid * mid * square_count
        mid = mid // 2

    return square_index

print(solution(N, r, c))

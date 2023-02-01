def solution(common):
    answer = 0
    if common[0] + common[2] == common[1] * 2:
        return common[-1] * 2 - common[-2]
    return common[-1] ** 2 / common[-2]


def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()
    tmp =  set(lost) & set(reserve)
    reserve = list(set(reserve) - tmp)
    lost = list(set(lost) - tmp)
    for i in lost:
        if i - 1 >= 1 and i - 1 in reserve:
            reserve.remove(i - 1)
        elif i + 1 <= n and i + 1 in reserve:
            reserve.remove(i + 1)
        else:
            answer -= 1
    return answer
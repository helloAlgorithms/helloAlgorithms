def solution(sides):
    cnt = 0
    for i in range(sum(sides)):
        if (max(sides) <= i):
            if max(sides) <= i < sum(sides):
                cnt += 1
        else:
            if sum([i, min(sides)]) > max(sides) and i < max(sides):
                cnt+= 1  
    return cnt

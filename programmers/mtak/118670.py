import copy
def solution(rc, operations):
    answer = [[0 for c in range(len(rc[0]))] for r in range(len(rc))]
    def ShiftRow(src, target):
        for idx in range(len(src)):
            idx = (idx + 1) % len(src) 
            for idxx in range(len(src[0])):
                target[idx][idxx] = src[idx - 1][idxx]
        return target
        
    def Rotate(src, target):
        target[0] = [src[1][0]] + src[0][:-1]
        for r in range(2, len(src)):
            target[r][-1] = src[r - 1] [-1]
        target[1][-1] = src[0][-1]
        target[-1] = src[-1][1:] + [src[-2][-1]]
        for r in range(1, len(src) - 2):
            target[r][0] = src[r + 1][0]
        target[-2][0] = src[-1][0]
        for r in range(1,len(src) - 1):
            for c in range(1, len(src[0]) - 1):
                target[r][c] = src[r][c]
        return target
        
    for f in operations:
        if f == "Rotate": rc = copy.deepcopy(Rotate(rc, answer))
        else: rc = copy.deepcopy(ShiftRow(rc, answer))
    return answer

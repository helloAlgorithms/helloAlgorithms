def solution(code):
    answer = ''
    mode = 0
    def zero(x):
        nonlocal answer
        nonlocal mode
        if code[x] != "1":
            if x % 2 == 0:
                answer += code[idx]
        else:
            mode = 1
    def one(x):
        nonlocal answer
        nonlocal mode
        if code[x] != "1":
            if x % 2 != 0:
                answer += code[idx]
        else:
            mode = 0
    f = {0: zero, 1:one}
    for idx in range(len(code)):
        f[mode](idx)
    if answer == "":
        return "EMPTY"
    return answer
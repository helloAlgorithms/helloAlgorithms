def solution(babbling):
    answer = 0
    poss = {"aya", "ye", "woo", "ma"}
    for t in babbling:
        idx = -1
        while True:
            for p in poss:
                idx = t.find(p)
                if idx == 0:
                    t = t[len(p):]
                    break
            if idx == 0:
                if t == "":
                    answer += 1
                    break
            else:break
    return answer

def solution(babbling):
    ongs = ["aya", "ye", "woo", "ma"]
    answer = 0
    idx = 0
    while idx < len(babbling):
        for o in ongs:
            babbling[idx] = babbling[idx].replace(o, "1")
        babbling[idx] = babbling[idx].replace("1", "")
        if not babbling[idx]:
            answer += 1
        idx += 1
    return answer
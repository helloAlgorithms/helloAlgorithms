def solution(my_string, target):
    idx = 0
    while idx <= len(my_string) - len(target):
        if target == my_string[idx:idx + len(target)]:return 1
        idx += 1
    return 0

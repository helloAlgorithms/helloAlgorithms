def solution(X, Y):
    common = set(X)&set(Y)
    answer = []
    if len(common) == 0:return "-1"
    for c in common:
        answer.extend([c] * min(X.count(c), Y.count(c)))
    answer = ''.join(sorted(list(answer), reverse=True))
    if answer[0]== "0": return "0"
    return answer
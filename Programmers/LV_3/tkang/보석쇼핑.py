# 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매
import collections
def solution2(gems):
    answer = []
    temp = list(set(gems))
    temp.sort()
    ans = (0, int(1e9))

    for i in range(len(gems)):
        last = -1
        dict = {}
        for j in range(i, len(gems)):
            dict[gems[j]] = 1
            if len(dict) == len(temp):
                last = j
                break
        if last != -1:
            if last - i < ans[1] - ans[0]:
                ans = (i, last)
    answer.append(ans[0] + 1)
    answer.append(ans[1] + 1)
    return answer

def solution(gems):
    answer = []
    temp_answer = int(1e9)
    temp = list(set(gems))
    temp.sort()
    lt = 0
    dict = collections.defaultdict(int)
    for rt in range(len(gems)):
        dict[gems[rt]] += 1
        while len(dict) == len(temp):
            if rt - lt < temp_answer:
                temp_answer = rt - lt
                answer = [lt + 1, rt + 1]
            dict[gems[lt]] -= 1
            if dict[gems[lt]] == 0:
                del dict[gems[lt]]
            lt += 1
    return answer

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
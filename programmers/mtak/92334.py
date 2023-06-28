def solution(id_list, report, k):
    chart = {id : [[], 0] for id in id_list}
    for r in report:
        userId, suedUserId = r.split()
        if suedUserId not in chart[userId][0]:
            chart[userId][0].append(suedUserId)
    for userID, value in chart.items():
        for suedUserId in value[0]:
            chart[suedUserId][1] += 1
    answer = [0] * len(id_list)
    for idx, userID in enumerate(chart):
        answer[idx] = len(list(filter(lambda userID: chart[userID][1] >= k, chart[userID][0])))
    return answer

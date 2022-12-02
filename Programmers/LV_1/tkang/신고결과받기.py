def findIdx(id_list, key):
    for i in range(len(id_list)):
        if key == id_list[i]:
            return i
    return None

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    reported = [0 for _ in range(len(id_list))]
    temp = {}
    banned = []
    for i in id_list:
        temp[i] = []
    for r in report:
        r1, r2 = r.split(' ')
        reported[findIdx(id_list, r2)] += 1
        temp[r1].append(r2)
    for i in range(len(id_list)):
        if reported[i] >= k:
            banned.append(id_list[i])
    banned.sort()
    key_lst = temp.keys()
    for k in key_lst:
        temp[k].sort()
        sum = 0
        for j in range(len(banned)):
            if banned[j] in temp[k]:
                sum += 1
        answer.append(sum)
    return answer
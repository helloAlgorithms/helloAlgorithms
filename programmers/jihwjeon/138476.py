def solution(k, tangerine):
    answer = 0
    d = {}
    
    for t in tangerine:
        if t not in d:
            d[t] = 1
        else:
            d[t] += 1
            
    d = sorted(d.items(), key=lambda item: item[1], reverse=True)
    
    tmp = 0
    for v, cnt in d:
        tmp += cnt
        answer += 1
        if tmp >= k:
            break
    return answer

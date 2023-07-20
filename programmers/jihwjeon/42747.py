def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    h = max(citations)
    
    while h:
        cnt = 0
        for x in citations:
            if x >= h:
                cnt += 1
                
        if cnt >= h:
            answer = h
            break
        h -= 1
    
    
    return answer

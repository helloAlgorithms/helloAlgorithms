def solution(queue1, queue2):
    f_sum, s_sum = sum(queue1) , sum(queue2)
    if (f_sum + s_sum) % 2 != 0:return -1
    h_sum = (f_sum + s_sum) / 2
    for i in [queue1, queue2]:
        if len(list(filter(lambda x:x > h_sum, i))) != 0:return -1
    answer = 0
    while True:
        if f_sum > h_sum:
            tmp = queue1.pop(0)
            queue2.append(tmp)
            f_sum -= tmp
            s_sum += tmp
            answer += 1
            continue
        elif f_sum == h_sum:break
        tmp = queue2.pop(0)
        queue1.append(tmp)
        f_sum += tmp
        s_sum -= tmp
        answer += 1
    return answer

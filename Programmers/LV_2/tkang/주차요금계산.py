# 기본 요금 + (단위 시간 * 단위 요금)
# 입차 후 출차 없으면 -> 23:59 출차
# 00:00 ~ 23:59 누적 주차
# 기본 시간 이하라면 기본 요금
# 기본 시간 초과 -> 기본요금 + 초과 시간 단위 요금

from collections import deque
import datetime
import math

def solution(fees, records):
    records_lst = []
    for r in records:
        a = r.split(' ')
        time, car_num, status = a[0], a[1], a[2]
        records_lst.append([time, car_num, status])
    records_lst.sort(key=lambda x: x[1])
    print(records_lst)
    dict = {}
    for i in range(len(records_lst)):
        in_time, in_car_num, in_status = records_lst[i]
        if i < len(records_lst) - 1 and in_status == 'IN' and records_lst[i + 1][2] == 'OUT':
            out_time, out_car_num, out_status = records_lst[i + 1]
            out_h, out_m = out_time.split(':')
            in_h, in_m = in_time.split(':')
            h = int(out_h) - int(in_h)
            m = int(out_m) - int(in_m)
            time = (h * 60) + m
            if in_car_num in dict:
                dict[in_car_num] += time
            else:
                dict[in_car_num] = time
        elif (i == len(records_lst) - 1 and in_status == 'IN') or in_status == 'IN' and records_lst[i + 1][2] != 'OUT' and (in_car_num != records_lst[i + 1][1]):
            in_h, in_m = in_time.split(':')
            h = 23 - int(in_h)
            m = 59 - int(in_m)
            time = (h * 60) + m
            if in_car_num in dict:
                dict[in_car_num] += time
            else:
                dict[in_car_num] = time
    ans = []
    for d in dict.items():
        car_num, time = d[0], d[1]
        print(car_num, time)
        if time > fees[0]:
            res = math.ceil((time - fees[0]) / fees[2]) * fees[3] + fees[1]
            ans.append(res)
        else:
            ans.append(fees[1])

    return ans

solution([180, 5000, 10, 600],
         ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])

def solution2(fees, records):
    answer = []
    temp = []
    my_dict = {}
    for r in records:
        time, car_num, status = r.split(' ')
        temp.append((time, car_num, status))
        my_dict[car_num] = 0
    temp.sort(key=lambda x: x[1])
    temp = deque(temp)

    for i in range(len(records)):
        if temp:
            t, c, s = temp.popleft()
            H1, M1 = t.split(':')
            if s == 'IN':
                if temp and temp[0][2] == 'OUT':
                    H2, M2 = temp[0][0].split(':')
                    my_dict[c] += (int(H2) - int(H1)) * 60 + (int(M2) - int(M1))
                    temp.popleft()
                else:
                    my_dict[c] += (23 - int(H1)) * 60 + (59 - int(M1))

    res = sorted(my_dict.items())
    for r in res:
        if r[1] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((r[1] - fees[0]) / fees[2]) * fees[3])
    return answer

def solution3(fees, records):
    answer = []
    inTime = [0] * 10000
    isIn = [0] * 10000
    sumT = [0] * 10000

    for record in records:
        a, b, c = record.split()
        h, m = a.split(":")
        if c == "IN":
            inTime[int(b)] = int(h) * 60 + int(m)
            isIn[int(b)] = 1
        else:
            sumT[int(b)] += int(h) * 60 + int(m) - inTime[int(b)]
            isIn[int(b)] = 0
    for i in range(10000):
        if isIn[i]:
            sumT[i] += (23*60+59) - inTime[i]
    for i in range(10000):
        if sumT[i] > 0:
            answer.append(fees[1] + max(math.ceil((sumT[i] - fees[0])/fees[2]), 0) * fees[3])
    return answer
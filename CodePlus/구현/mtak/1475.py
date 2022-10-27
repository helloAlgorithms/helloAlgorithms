import math
n = input().strip()
dic = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
for i in n:
    if i == '9':
        dic[6] += 1
    else:
        dic[int(i)] += 1
t = dic[6] / 2
del dic[6]
print(max(max(dic.values()), math.ceil(t)))



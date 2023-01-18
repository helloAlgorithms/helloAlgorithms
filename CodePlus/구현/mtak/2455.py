tmp = 0
stat = []
for i in range(4):
    m,p = map(int, input().split())
    tmp -= m
    tmp += p
    stat.append(tmp)
print(max(stat))

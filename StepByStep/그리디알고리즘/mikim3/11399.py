# 시작시간 4시35분
n = int(input())

li = list(map(int,input().split()))
total = 0
li.sort()
wait_time = 0
for i in range(n):
    total += wait_time + li[i]
    wait_time += li[i]
print(total)

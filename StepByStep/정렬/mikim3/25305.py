# 시작시간 10:42  # 마무리시간 10:44
n,k = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
print(li[-k])

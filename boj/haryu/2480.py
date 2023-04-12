# https://www.acmicpc.net/problem/2480

print("My version")
dice = [0] * 6
a, b, c = list(map(int, input().split()))
dice[a - 1] += 1
dice[b - 1] += 1
dice[c - 1] += 1
max_num = 1
for j in dice:
  if max_num < j:
    max_num = j 

if max_num == 1:
  print(max(a, max(b, c)) * 100)
elif max_num == 2:
  print(1000 + (a*100)) if a == c else print(1000 + (b*100))
else :
  print(10000 + (a*1000))

# 최적화 극한으로 한 경우 
# 파이썬은 삼단으로 조건 확인해도 되는 듯?
# 삼항연산자를 적극 활용함 [ture] if condition else [false]
#print("boj version")
# a, b, c=map(int, input().split())
# print(10000+1000*a if a==b==c else 1000+100*b if a==b or b==c else 1000+100*a if c==a else 100*max(a, b, c))
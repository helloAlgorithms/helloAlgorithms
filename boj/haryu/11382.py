# https://www.acmicpc.net/problem/11382
import sys

# line = sys.stdin.readline().rstrip()
# arr = ["" , "" , ""]

# limit = len(line)
# i = 0
# j = 0
# while j < limit:
#   if line[j] == ' ':
#     i+=1
#   elif line[j] != ' ' :
#     arr[i] += line[j]
#   j += 1

# a = int(arr[0])
# b = int(arr[1])
# c = int(arr[2])

# print(a + b + c)

# 보다 나은 버전 1
# line = map(int, (sys.stdin.readline().rstrip()).split())
# print(sum(line))

# 보다 나은 버전 2 속도 개선 없음
#print(sum(map(int, (sys.stdin.readline().rstrip()).split())))

# 보다 나은 버전 3 속도개선 됨 
print(sum(map(int, input().split())))

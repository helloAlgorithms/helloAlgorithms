# ai + aj = x 쌍
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
x = int(input())

lst.sort()

lt = 0
rt = n - 1
answer = 0

while lt < rt:
	sum = lst[lt] + lst[rt]
	if sum == x:
		answer += 1
	elif sum < x:
		lt += 1
		continue
	rt -= 1
print(answer)
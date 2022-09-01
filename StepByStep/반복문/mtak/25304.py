import sys
input = sys.stdin.readline
x = int(input())
n = int(input())
sum = 0
for _ in range(n):
    p, cnt = map(int, input().split())
    sum += (p * cnt)
if x == sum:
    print("Yes")
else:
    print("No")


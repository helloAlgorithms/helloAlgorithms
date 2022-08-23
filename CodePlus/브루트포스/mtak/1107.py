import sys
input = sys.stdin.readline
n = int(input())
ans = abs(100 - n)
m = int(input())
b = set(map(int, input().split()))
h = 0
for num in range(1000001):
    for idx, j in enumerate(str(num)):
        if int(j) in b:
            break
        elif idx == len(str(num)) - 1:
            ans = min(ans, len(str(num)) + abs(num - n))
            h = num
print(ans)
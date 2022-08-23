import sys
input = sys.stdin.readline
n = int(input())
ans = abs(100 - n)
m = int(input())
b = set(map(int, input().split()))
for num in range(1000001):
    for j in str(num):
        if j in b:
            break
        else:
            ans = min(ans, len(str(num)) + abs(num - n))
            h = num
print(ans)

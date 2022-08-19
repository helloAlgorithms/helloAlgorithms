import sys
input = sys.stdin.readline
n = int(input())
ans = abs(100 - n)
m = int(input())
b = set(range(10))
if m > 0:
	b = b -set(map(int, input().split()))
for num in range(1000001):
    for j in str(num):
        if j not in b:
            break
        else:
            ans = min(ans, len(str(num)) + abs(num - n))
print(ans)

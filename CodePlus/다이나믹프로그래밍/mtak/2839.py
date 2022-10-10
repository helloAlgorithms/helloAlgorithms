import sys
input = sys.stdin.readline
n = int(input())
arr = [5001] * (n + 5)
arr[3] , arr[5] = 1, 1
for i in range(6, n + 1):
    arr[i] = min(arr[i - 3], arr[i - 5]) + 1
print(arr[n] if arr[n] < 5001 else -1)

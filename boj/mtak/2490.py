import sys
input = sys.stdin.readline
a = ['A', 'B', 'C', 'D', 'E']
for _ in range(3):
    print(a[3 - sum(list(map(int, input().split())))])

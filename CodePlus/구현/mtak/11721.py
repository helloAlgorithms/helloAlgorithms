import sys
input = sys.stdin.readline
line = input().strip()
for i in range(0,len(line), 10):
    print(line[i:i + 10])


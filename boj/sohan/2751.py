import sys
N = int(input())
numbers = [int(sys.stdin.readline()) for i in range(N)]
print('\n'.join(map(str, sorted(numbers))))

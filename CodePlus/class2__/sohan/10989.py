import sys
N = int(input())
numbers = [0 for i in range(10001)]
for index in range(N):
    numbers[int(sys.stdin.readline().strip('\n'))] += 1;
for index, num in enumerate(numbers):
    if (num != 0): 
        for i in range(num): print(index)

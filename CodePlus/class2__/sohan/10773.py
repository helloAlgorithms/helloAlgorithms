import sys
K = int(input())
numbers = [int(sys.stdin.readline().strip('\n')) for i in range(K)]
numlist = []
for num in numbers:
    if num == 0:
        numlist.pop()
    else : numlist.append(num)

print(sum(numlist))

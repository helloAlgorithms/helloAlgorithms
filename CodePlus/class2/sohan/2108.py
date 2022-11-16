from collections import Counter
import sys

N = int(input())
numbers = [int(sys.stdin.readline()) for i in range(N)]
snum = sorted(numbers)
count = Counter(snum)
print(round(sum(numbers) / N))
print(snum[N // 2])
mode = count.most_common()
try:
    if (mode[0][1] == mode[1][1]):
        print(mode[1][0])
    else:
        print(mode[0][0])
except:
    print(mode[0][0])
print(snum[N - 1] - snum[0])

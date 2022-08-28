import sys
input = sys.stdin.readline
dobiHeight = [int(input()) for _ in range(9)]
sum = 0
realDobi = []
for i in dobiHeight:
    sum += i
for i in range(8):
    for k in range(i + 1, 9):
        if (sum - (dobiHeight[i] + dobiHeight[k])) == 100:
            for j in range(9):
                if (j == i or j == k):
                    continue
                realDobi.append(dobiHeight[j])
            for p in sorted(realDobi):
                print(p)
            exit()

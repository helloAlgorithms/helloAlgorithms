#
# for j in range(9): 라고 풀어서 오래걸렸다.
import sys

input = sys.stdin.readline

li = []
for i in range(9):
    li.append(int(input()))
for i in range(9):
    for j in range(i+1, 9):
        if sum(li) - (li[i] + li[j]) == 100:
            li[i],li[j] = -1, -1
li.sort()

for i in range(2,9):
    print(li[i])


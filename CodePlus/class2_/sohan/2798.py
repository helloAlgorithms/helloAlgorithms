from itertools import combinations

N, M = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))
comb = list(combinations(numbers, 3))
answer = []
for item in comb:
    summ = sum(item)
    if summ <= M:
        answer.append(summ)
print(max(answer))

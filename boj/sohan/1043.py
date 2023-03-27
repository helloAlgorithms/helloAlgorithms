N, M = map(int, input().split(' '))
truth = set(input().split(' ')[1:])
count = 0
party = []

for _ in range(M):
    party.append(set(input().split(' ')[1:]))

for _ in range(M):
    for p in party:
        if p & truth:
            truth |= p

for p in party:
    if not p & truth:
        count += 1

print(count)
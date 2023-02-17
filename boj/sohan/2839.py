N = int(input())
pair = []

for x in range (N):
    y = (N - 3*x) // 5
    if y < 0: break
    if (N - 3*x) % 5 == 0:
        pair.append(x + y)

print("-1" if len(pair) == 0 else min(pair))

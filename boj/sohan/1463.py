N = int(input())

min_count = [0] * (N + 1)

for i in range(2, N + 1):
    
    min_count[i] = min_count[i - 1] + 1

    if i % 2 == 0:
        min_count[i] = min(min_count[i], min_count[i // 2] + 1)
    if i % 3 == 0:
        min_count[i] = min(min_count[i], min_count[i // 3] + 1)

print(min_count[N])

N = int(input())

house = [list(map(int, input().split(' '))) for _ in range(N)]

for i in range(1, N):
    house[i][0] += min(house[i - 1][1], house[i - 1][2])
    house[i][1] += min(house[i - 1][0], house[i - 1][2])
    house[i][2] += min(house[i - 1][0], house[i - 1][1])

print(min(house[-1]))
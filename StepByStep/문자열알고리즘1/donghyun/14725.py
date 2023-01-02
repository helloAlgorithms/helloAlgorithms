from collections import defaultdict

nested = lambda: defaultdict(nested)
food_info = nested()
for _ in range(int(input())):
    floor = food_info
    for food in input().split()[1:]:
        floor = floor[food]
def dfs(floor, depth):
    for next_floor in sorted(floor):
        print("--"*depth+next_floor)
        dfs(floor[next_floor], depth + 1)
dfs(food_info, 0)
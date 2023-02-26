a = list(map(int, input().strip().split(" ")))
def insertion_sort(a):
    for edge in range(1, len(a)):
        for target in range(edge, 0, -1):
            if a[target - 1] > a[target]:
                a[target - 1] , a[target] = a[target], a[target - 1]
insertion_sort(a)
for p in a:
    print(p, end="")
    if p != a[-1]:
        print(" ", end="")


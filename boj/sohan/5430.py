from collections import deque

T = int(input())

for _ in range(T):
    fn = list(input())
    n = int(input())
    try:
        arr = deque(map(int, input().strip("[]").split(',')))
    except:
        arr = []
    r = -1
    err = ""

    for f in fn:
        if f == 'R':
            r *= -1
        elif f == 'D':
            if len(arr) == 0:
                err = "error"
                break
            if r == 1:
                arr.pop()
            else:
                arr.popleft()

    if err != "":
        print(err)
    else:
        print("[", end="")
        if r == 1:
            print(*reversed(arr), sep = ",", end = "]\n")
        else:
            print(*arr, sep = ",", end = "]\n")
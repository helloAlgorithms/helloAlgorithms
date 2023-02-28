import sys
input = sys.stdin.readline
cnt = int(input())
for _ in range(cnt):
    a = input().strip()
    s = []
    flag = 0
    for i in a:
        if i == ")":
            if len(s) == 0:
                flag = 1
                break
            s.pop()
            continue
        s.append(")")
    if len(s) != 0:
        flag = 1
    print("YES" if flag == 0 else "NO")

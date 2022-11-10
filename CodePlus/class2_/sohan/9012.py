N = int(input())
strings = [list(input()) for i in range(N)]
for string in strings:
    end = 0
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                print("NO")
                end = -1
                break
            stack.pop()
    if (end != -1):
        print("YES" if len(stack) == 0 else "NO")

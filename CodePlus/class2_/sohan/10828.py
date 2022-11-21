import sys
N = int(input())
stack = []
for count in range(N):
    line = sys.stdin.readline().strip()
    command = line.split(' ')
    if (command[0] == "push"):
        stack.append(command[1])
    elif command[0] == "top":
        if (len(stack) == 0):
            print(-1)
        else : print(stack[-1])
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(1 if len(stack) == 0 else 0)
    elif command[0] == "pop":
        if (len(stack) == 0):
            print(-1)
        else:
            print(stack.pop())

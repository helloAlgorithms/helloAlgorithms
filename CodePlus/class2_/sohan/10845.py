import sys
N = int(input())
queue = []
for i in range(N):
    line = sys.stdin.readline().strip()
    command = line.split()
    if (command[0] == "push"):
        queue.append(command[1])
    elif command[0] == "front":
        if (len(queue) == 0):
            print(-1)
        else : print(queue[0])
    elif command[0] == "back":
        if (len(queue) == 0):
            print(-1)
        else : print(queue[-1])
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(1 if len(queue) == 0 else 0)
    elif command[0] == "pop":
        if (len(queue) == 0):
            print(-1)
        else:
            print(queue.pop(0))

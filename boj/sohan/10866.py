import sys
N = int(input())
deque = []
for i in range(N):
    line = sys.stdin.readline().strip()
    command = line.split()
    if command[0] == "push_front":
        deque.insert(0, command[1])
    elif (command[0] == "push_back"):
        deque.append(command[1])
    elif command[0] == "front":
        if (len(deque) == 0):
            print(-1)
        else : print(deque[0])
    elif command[0] == "back":
        if (len(deque) == 0):
            print(-1)
        else : print(deque[-1])
    elif command[0] == "size":
        print(len(deque))
    elif command[0] == "empty":
        print(1 if len(deque) == 0 else 0)
    elif command[0] == "pop_front":
        if (len(deque) == 0):
            print(-1)
        else:
            print(deque.pop(0))
    elif command[0] == "pop_back":
        if (len(deque) == 0):
            print(-1)
        else:
            print(deque.pop())

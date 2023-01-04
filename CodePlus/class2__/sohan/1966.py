N = int(input())
infos = []
queues = []
for i in range(N):
    infos.append(list(map(int, input().split(' '))))
    queues.append(list(map(int, input().split(' '))))

for info,queue in zip(infos,queues):
    index = info[1]
    answer = 0

    eq = list(enumerate(queue))
    while True:
        if (sum(1 for item in queue if item > queue[0])):
            queue.append(queue.pop(0))
            eq.append(eq.pop(0))
        else :
            answer = answer + 1
            queue.pop(0)
            if (eq.pop(0)[0] == index):
                print(answer)
                break

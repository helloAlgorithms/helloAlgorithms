N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
adjs = [[] for _ in range(N)]
counts = []

for edge in edges:
    adjs[edge[0] - 1].append(edge[1])
    adjs[edge[1] - 1].append(edge[0])

def tracking(start, adjs):
    queue = []
    predecessor = [-1 for _ in range(N)]
    visited = [0 for _ in range(N)]
    
    queue.append(start)
    visited[start] = 1

    while len(queue) != 0:
        index = queue.pop(0)
        for user in adjs[index]:
            if visited[user - 1] == 0:
                visited[user - 1] = 1
                predecessor[user - 1] = index
                queue.append(user - 1)
    count = 0
    for dest in range(N):
        index = dest
        while predecessor[index] != -1:
            index = predecessor[index]
            count += 1
    
    return count

for index in range(N):
    counts.append(tracking(index, adjs))

print(counts.index(min(counts)) + 1)

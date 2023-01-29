import sys
sys.setrecursionlimit(10 ** 6)

N, M, V = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x:x[0])
adjacents = [[] for _ in range(N)]
visited = [0 for _ in range(N)]
answer = ""

for edge in edges:
    adjacents[edge[0] - 1].append(edge[1])
    adjacents[edge[1] - 1].append(edge[0])

for adjacent in adjacents:
    adjacent.sort()

def DFS(adjacents, index, visited, answer):
    if visited[index] == 1:
        return answer
    visited[index] = 1
    answer += str(index + 1) + " "
    for vertex in adjacents[index]:
        answer = DFS(adjacents, vertex - 1, visited, answer)
    return answer

def BFS(adjacents, index, visited, answer):
    queue = []
    queue.append(index + 1)
    visited[index] = 1
    while len(queue) != 0:
        index = queue.pop(0) - 1
        answer += str(index + 1) + " "
        for vertex in adjacents[index]:
            if visited[vertex - 1] == 0:
                visited[vertex - 1] = 1
                queue.append(vertex)
    return answer


answer = DFS(adjacents, V - 1, visited, answer)
print(answer.strip())
answer = ""
visited = [0 for _ in range(N)]
answer = BFS(adjacents, V - 1, visited, answer)
print(answer.strip())

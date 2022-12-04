from collections import deque

def solution(n, wires):
    graph = [[] * (n + 1) for _ in range(n + 1)]

    for w in wires:
        graph[w[0]].append(w[1])
        graph[w[1]].append(w[0])

    ans = int(1e9)
    for i in range(1, n + 1):
        visited = [0] * (n + 1)
        q = deque([1])
        visited[i] = 1
        cnt = 0
        while q:
            a = q.pop()
            visited[a] = 1
            for j in range(len(graph[a])):
                if not visited[graph[a][j]]:
                    q.append(graph[a][j])
            cnt += 1
        ans = min(ans, abs((n - cnt) - cnt))
    return ans

solution(7,	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])

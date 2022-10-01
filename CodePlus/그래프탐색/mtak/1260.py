n, m, v = map(int, input().split())
_map = {}
for _ in range(1, n + 1):
    _map[_] = []
for _ in range(m):
    x, y = map(int, input().split())
    _map.get(x).append(y)
    _map.get(y).append(x)
def bfs(v):
    visit = list()
    queue = list()
    queue.append(v)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(sorted(_map[node]))
    return visit

def dfs(v):
    visit = list()
    stack = list()
    stack.append(v)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            _map[node].sort()
            _map[node].reverse()
            stack.extend(_map[node])
    return visit
for p in dfs(v):
    print(p, end = " ")
print()
for p in bfs(v):
    print(p, end = " ")

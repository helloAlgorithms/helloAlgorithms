import sys
sys.setrecursionlimit(10**6)

T = int(input())
answer = []

def visit_baechu(baechus, baechu_index, baechu_visited):
    baechu_visited[baechu_index] = 1
    for baechu in baechus[baechu_index]:
        if baechu_visited[baechu] == 0:
            visit_baechu(baechus, baechu, baechu_visited)

for _ in range(T):
    M, N, K = list(map(int, input().split()))
    baechu_coordinates = [list(map(int, input().split())) for _ in range(K)]
    baechu_coordinates.sort(key = lambda x:(x[0], x[1]))
    baechu_adj = [[] for _ in range(K)]
    baechu_visited = [0 for _ in range(K)]
    index = 0
    for col, row in baechu_coordinates:
            up = [col, row - 1]
            down = [col, row + 1]
            left = [col - 1, row]
            right = [col + 1, row]

            if up in baechu_coordinates:
                baechu_adj[index].append(baechu_coordinates.index(up))
            if down in baechu_coordinates:
                baechu_adj[index].append(baechu_coordinates.index(down))
            if left in baechu_coordinates:
                baechu_adj[index].append(baechu_coordinates.index(left))
            if right in baechu_coordinates:
                baechu_adj[index].append(baechu_coordinates.index(right))
            index += 1

    worm_count = 0
    while 0 in baechu_visited:
        baechu_index = baechu_visited.index(0)
        visit_baechu(baechu_adj, baechu_index, baechu_visited)
        worm_count += 1
    answer.append(worm_count)

for _ in answer:
    print(_)

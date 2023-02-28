from collections import deque

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
counts = [0,0,0]
q = deque()

def count(paper, q):
    N = q[0][2]
    p = [[-1] * N] * N

    if p == paper:
        counts[0] += 1
        q[1] = True

    p = [[0] * N] * N
    if p == paper:
        counts[1] += 1
        q[1] = True

    p = [[1] * N] * N
    if p == paper:
        counts[2] += 1
        q[1] = True

    return q

q.append(count([d[0:N] for d in paper[0:N]], [[0,0,N], False]))

while len(q) != 0:
    p = q.popleft()
    row = p[0][0]
    col = p[0][1]
    step = p[0][2] // 3
    
    if p[1] == False and step != 0:
        if step == 1:
            for i in range(row, row + step * 3, step):
                for j in range(col, col + step * 3, step):
                    counts[0] += (paper[i][j] == -1)
                    counts[1] += (paper[i][j] == 0)
                    counts[2] += (paper[i][j] == 1)
        else:
            for i in range(row, row + step * 3, step):
                for j in range(col, col + step * 3, step):
                    q.append(count([d[j:j + step] for d in paper[i:i + step]], [[i,j,step], False]))

for c in counts:
    print(c)


def solution(A, row, col) -> list:
    max = -1
    max_row = -1
    max_col = -1
    for i in range(row):
        for j in range(col):
            if A[i][j] > max:
                max = A[i][j]
                max_row = i
                max_col = j
    return [max, max_row+1, max_col+1]

def runtime() -> None:
    matrix = [];
    for i in range(9):
        matrix.append(list(map(int, input().split())))
    ans = solution(matrix, 9, 9)
    print(ans[0])
    print(ans[1], ans[2])

runtime()
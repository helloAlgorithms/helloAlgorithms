def solution(A, B, row, col) -> list:
    C = [[0] * col for i in range(row)]
    for i in range(row):
        for j in range(col):
            C[i][j] = A[i][j] + B[i][j]
    return C

def print_matrix(matrix) -> None:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()

def runtime() -> None:
    row, col = map(int, input().split())
    A = []
    B = []
    for i in range(row):
        A.append(list(map(int, input().split())))
    for i in range(row):
        B.append(list(map(int, input().split())))
    ans = solution(A, B, row, col)
    print_matrix(ans)

runtime()
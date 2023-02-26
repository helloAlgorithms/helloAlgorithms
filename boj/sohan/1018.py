N, M = map(int, input().split(' '))
board = [list(input()) for i in range(N)]

WB = ['W','B','W','B','W','B','W','B']
BW = ['B','W','B','W','B','W','B','W']

white = [WB,BW,WB,BW,WB,BW,WB,BW]
black = [BW,WB,BW,WB,BW,WB,BW,WB]

def cut_board(board, i, j):
    new_board = list(board[row][i:i + 8] for row in range(j,j + 8))
    return new_board

def count_paint(board):
    count_white = 0
    count_black = 0
    for ai, bi, ci in zip(board, white, black):
        for ci, di, ei in zip(ai, bi, ci):
            count_white += (ci != di)
            count_black += (ci != ei)
    return min(count_white, count_black)

def solution(board):
    col_max = M - 7
    row_max = N - 7
    answer = []
    for j in range(row_max):
        for i in range(col_max):
            answer.append(count_paint(cut_board(board, i, j)))
    return (sorted(answer)[0])

print(solution(board))

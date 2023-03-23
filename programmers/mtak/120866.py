def solution(board):
    answer = 0
    width = len(board[0])
    height = len(board)
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [1, 0, -1, 1, -1, 1, 0, -1]
    for r in board:
        print(r)
    print()
    for rn, r in enumerate(board):
        for cn, c in enumerate(r):
            if c == 0 or c != 1: continue
            for i in range(8):
                nx = dx[i] + cn
                ny = dy[i] + rn
                if  not( 0 <= nx <  width) or not( 0 <= ny <  height) or board[ny][nx] == 1: continue
                board[ny][nx] = 2
    for r in board:
        print(r)
        answer += r.count(0)   
    return answer

got = 	[[0, 0, 0], [0, 1, 0], [0, 0, 0]]
got = 	[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
got = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
got = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
solution(got)
import Foundation

func solution(_ board:[[Int]]) -> Int {
    var answer:Int = 0
    var board = board
    if board.count == 1 || board[0].count == 1 { return 1 }

    for i in 0..<board.count {
        for j in 0..<board[0].count {
            if board[i][j] == 1 && i > 0 && j > 0 {
                if board[i - 1][j] == 0 || board[i - 1][j - 1] == 0 || board[i][j - 1] == 0 { board[i][j] = 1 }
                board[i][j] = min(min(board[i - 1][j], board[i - 1][j - 1]), board[i][j - 1]) + 1
                if board[i][j] * board[i][j] > answer { answer = board[i][j] * board[i][j] }
            }
        }
    }
    return answer
}

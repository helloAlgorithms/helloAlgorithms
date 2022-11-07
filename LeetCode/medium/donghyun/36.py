class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_set = set()
            for n in row:
                if n != "." and n in row_set:
                    return False
                row_set.add(n)
        
        for col in zip(*board):
            col_set = set()
            for n in col:
                if n != "." and n in col_set:
                    return False
                col_set.add(n)
                
        for k in ((0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)):
            square_set = set()
            for i in range(3):
                for j in range(3):
                    n = board[k[0]+i][k[1]+j]
                    if n != "." and n in square_set:
                        return False
                    square_set.add(n)
        
        return True
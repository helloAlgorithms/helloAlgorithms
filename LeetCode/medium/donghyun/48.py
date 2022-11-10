class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        tmp = []
        for col in zip(*matrix):
            tmp.append(col[::-1])
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = tmp[i][j]
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        reshape = [[0] * c for _ in range(r)]
        i = 0
        for row in mat:
            for col in row:
                reshape[i//c][i%c] = col
                i += 1
        return reshape
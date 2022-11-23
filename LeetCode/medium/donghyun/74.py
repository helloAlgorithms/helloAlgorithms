class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if (idx:=bisect_left(matrix[i], target)) == n:
                continue
            elif matrix[i][idx] == target:
                return True
        return False
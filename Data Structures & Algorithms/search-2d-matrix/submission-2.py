class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        a, b = 1, m * n
        if matrix[0][0] == target or matrix[m-1][n-1] == target:
            return True
        while b-a > 1:
            c = a + int((b-a)/2)
            i, j = (c-1) // n, (c-1) % n
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                b = c
            else:
                a = c
        return False

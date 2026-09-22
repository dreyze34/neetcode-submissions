class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        m = len(trust)
        for a, b in trust:
            matrix[a-1][b-1] = 1

        for i in range(n):
            line = matrix[i]
            col = [matrix[j][i] for j in range(n) if j != i]
            if not any(line) and all(col):
                return i+1
        return -1
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)]]
        dp[0][0] = 1 if not obstacleGrid[0][0] else 0
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] if not obstacleGrid[0][i] else 0
        for j in range(1, m):
            el = dp[j-1][0] if not obstacleGrid[j][0] else 0
            dp.append([el] + [0 for _ in range(n-1)])
        for i in range(1, m):
            for j in range(1, n):
                left = dp[i][j-1] if not obstacleGrid[i][j-1] else 0
                up = dp[i-1][j] if not obstacleGrid[i-1][j] else 0
                dp[i][j] = left + up if not obstacleGrid[i][j] else 0
        return dp[-1][-1]
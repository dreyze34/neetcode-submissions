class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[grid[0][0]]]
        for i in range(1, n):
            dp[0].append(dp[0][-1] + grid[0][i])
        for j in range(1, m):
            line = [dp[j-1][0] + grid[j][0]] + [0 for _ in range(n-1)]
            dp.append(line)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
        return dp[-1][-1]
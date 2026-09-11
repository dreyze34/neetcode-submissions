class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        dp.append([1 for _ in range(n)])
        for _ in range(m-1):
            line = [int(i == 0) for i in range(n)]
            dp.append(line)
        for i in range(1, n):
            for j in range(1, m):
                dp[j][i] = dp[j-1][i] + dp[j][i-1]
        return dp[-1][-1]
                

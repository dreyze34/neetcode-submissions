class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1 if int(s[0]) else 0
        dp = [0 for _ in range(n)]
        if int(s[0]) == 0:
            return 0
        if 10 <= int(s[:2]) <= 26:
            dp[0] = 1
            if int(s[1]) != 0:
                dp[1] = 2
            else:
                dp[1] = 1
        else:
            if int(s[1]) != 0:
                dp[0] = 1
                dp[1] = 1
        for i in range(2, n):
            if int(s[i]) != 0:
                dp[i] += dp[i-1]
                if 10 <= int(s[i-1:i+1]) <= 26:
                    dp[i] += dp[i-2]
            else:
                if 10 <= int(s[i-1:i+1]) <= 26:
                    dp[i] += dp[i-2]
        return dp[-1]
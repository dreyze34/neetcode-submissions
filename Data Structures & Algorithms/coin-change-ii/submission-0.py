class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for c in coins:
            for target in range(1, amount + 1):
                if target - c >= 0:
                    dp[target] += dp[target - c]
        return dp[-1]

        
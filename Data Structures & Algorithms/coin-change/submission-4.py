class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [0]
        for curAmount in range(1, amount+1):
            numCoins = []
            for c in coins:
                if curAmount-c >= 0:
                    numCoin = dp[curAmount-c]
                    if numCoin != -1:
                        numCoins.append(numCoin)
            if not numCoins:
                dp.append(-1)
            else:
                dp.append(1+min(numCoins))
        return dp[-1]
            

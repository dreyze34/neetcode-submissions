class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        maxProfit = 0
        for i in range(1, n):
            maxProfit += max(prices[i]-prices[i-1], 0)
        return maxProfit

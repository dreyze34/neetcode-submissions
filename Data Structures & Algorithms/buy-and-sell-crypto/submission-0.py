class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max = 0
        if n == 1:
            return max
        buy = 0
        for i in range(n):
            cur = prices[i] - prices[buy]
            if cur > max:
                max = cur
            if cur < 0:
                buy = i
        return max

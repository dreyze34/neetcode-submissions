class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        held = [0 for _ in range(n)]
        held[0] = -prices[0]
        reset = [0 for _ in range(n)]
        sold = [0 for _ in range(n)]
        for i in range(1, n):
            held[i] = max(held[i-1], reset[i-1] - prices[i])
            sold[i] = prices[i] + held[i-1]
            reset[i] = max(reset[i-1], sold[i-1])
        return max(held[-1], sold[-1], reset[-1])
                
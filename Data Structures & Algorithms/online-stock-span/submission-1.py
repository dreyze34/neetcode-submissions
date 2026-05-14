class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        n = len(self.stack)
        i = 1
        while i <= n-1 and self.stack[-(i+1)] <= price:
            i += 1
        return i

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
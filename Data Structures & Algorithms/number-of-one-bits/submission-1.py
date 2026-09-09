class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        for i in range(32, -1, -1):
            if n >= 2**i:
                c += 1
                n = n - 2**i
        return c
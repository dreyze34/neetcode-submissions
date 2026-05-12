import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        a, b = 1, max(piles)
        k = b
        while a <= b:
            c = (a + b) // 2
            time = 0
            for i in range(n):
                time += math.ceil(piles[i]/c)
            print(a, b, c, time)
            if time > h:
                a = c + 1
            else:
                b = c - 1
                k = min(k, c)
        return k

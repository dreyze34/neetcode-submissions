import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        revertStones = [-s for s in stones]
        heapq.heapify(revertStones)
        while len(revertStones) > 1:
            x, y = -heapq.heappop(revertStones), -heapq.heappop(revertStones)
            if x > y:
                heapq.heappush(revertStones, y - x)
            elif x > y:
                heapq.heappush(revertStones, x - y)
        return -revertStones[-1] if revertStones else 0


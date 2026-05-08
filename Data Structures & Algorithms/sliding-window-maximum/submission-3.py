import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        numsInv = [-el for el in nums]
        heap = [(el, i) for i, el in enumerate(numsInv[:k])]
        heapq.heapify(heap)
        result = [-heap[0][0]]
        n = len(nums)
        for i in range(k, n):
            heapq.heappush(heap, (numsInv[i], i))
            candidate = heap[0]
            while candidate[1] < i-k+1:
                heapq.heappop(heap)
                candidate = heap[0]
            result.append(-candidate[0])
        return result
            








        
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distOrigin(x, y):
            return (x**2 + y**2)**(1/2)
        heap = []
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            dist = distOrigin(x, y)
            heapq.heappush(heap, (dist, i))
        kClosest = heapq.nsmallest(k, heap)
        return [points[i] for _, i in kClosest]

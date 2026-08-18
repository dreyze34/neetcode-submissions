class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n-1
        maxA = 0
        while i < j:
            curA = min(heights[i], heights[j]) * (j-i)
            maxA = max(curA, maxA)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return maxA
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n-1
        max = 0
        while i < j:
            cur = (j-i)*min(heights[i], heights[j])
            if cur > max:
                max = cur
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return max
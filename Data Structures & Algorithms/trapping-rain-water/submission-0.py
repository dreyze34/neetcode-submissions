class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lefts, rights = [0]*n, [0]*n
        maxL, maxR = 0, 0
        for i in range(1, n):
            if height[i-1] > maxL:
                maxL = height[i-1]
            lefts[i] = maxL
        for j in range(n-2, -1, -1):
            if height[j+1] > maxR:
                maxR = height[j+1]
            rights[j] = maxR

        areas = [0]*n
        for k in range(n):
            areas[k] = min(lefts[k], rights[k]) - height[k]

        print(areas)
        maxA = 0
        cur = 0
        for l in range(n):
            print(l, areas[l], cur)
            if areas[l] <= 0:
                maxA += cur
                cur = 0
            else:
                cur += areas[l]
        return maxA




        
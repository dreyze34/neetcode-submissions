class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        counts = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if i-1 >= 0:
                        counts[i-1][j] += 1
                    if j-1 >= 0:
                        counts[i][j-1] += 1
                    if i+1 <= m-1:
                        counts[i+1][j] += 1
                    if j+1 <= n-1:
                        counts[i][j+1] += 1
        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    perimeter += 4 - counts[i][j]
        return perimeter
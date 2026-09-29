class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        def dfs(i, j):
            stack = [(i, j)]
            visited.add((i, j))
            area = 0
            while stack:
                k, l = stack.pop()
                area += 1
                for di, dj in directions:
                    ni, nj = k + di, l + dj
                    if (
                        0 <= ni < m
                        and 0 <= nj < n
                        and grid[ni][nj]
                        and (ni, nj) not in visited
                    ):
                        stack.append((ni, nj))
                        visited.add((ni, nj))
            return area

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in visited:
                    max_area = max(max_area, dfs(i, j))
        return max_area


            

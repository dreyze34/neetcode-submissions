class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            stack = [(i, j)]
            while stack:
                k, l = stack.pop()
                visited.add((k, l))
                if k - 1 >= 0 and (k-1, l) not in visited and grid[k-1][l] == "1":
                    stack.append((k-1, l))
                if l - 1 >= 0 and (k, l-1) not in visited and grid[k][l-1] == "1":
                    stack.append((k, l-1))
                if k + 1 < m and (k+1, l) not in visited and grid[k+1][l] == "1":
                    stack.append((k+1, l))
                if l + 1 < n and (k, l+1) not in visited and grid[k][l+1] == "1":
                    stack.append((k, l+1))

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    result += 1
                    dfs(i, j)
        return result
            
            
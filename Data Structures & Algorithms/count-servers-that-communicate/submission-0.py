class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        line = [0 for _ in range(m)]
        for i in range(m):
            line[i] = sum(grid[i]) if sum(grid[i]) > 1 else 0

        col = [0 for _ in range(n)]
        for j in range(n):
            deduce = 0
            s = 0
            for i in range(m):
                if grid[i][j]:
                    s += 1
                    if line[i]:
                        deduce += 1
            if s > 1:
                col[j] = max(0, s - deduce)
        return sum(line) + sum(col)

            

            

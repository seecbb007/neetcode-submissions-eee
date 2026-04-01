class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[0,-1],[-1,0]]
        res = 0
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0 
            grid[r][c] = -1
            curr_area = 1
            for dr,dc in directions:
                newr = dr + r
                newc = dc + c
                curr_area += dfs(newr,newc)

            return curr_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c))
        return res 




        
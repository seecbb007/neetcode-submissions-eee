class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        

        def dfs(r,c, visited, prevHeight):
            if r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < prevHeight or (r,c) in visited:
                return 

            visited.add((r,c))

            for dr,dc in directions:
                newr = dr + r
                newc = dc + c

                dfs(newr, newc, visited, heights[r][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        for c in range(cols):
            dfs(0, c, pac,heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])    

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                newr = dr + r
                newc = dc + c

                if newr < 0 or newr >= rows or newc < 0 or newc >= cols:
                    continue

                if grid[newr][newc] == 2147483647:
                    grid[newr][newc] = grid[r][c] + 1
                    q.append((newr, newc))
                    


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        q = deque()
        fresh = 0 
        time = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    newr = dr + r
                    newc = dc + c
                    if 0 <= newr < rows and 0 <= newc < cols and grid[newr][newc] == 1:
                        grid[newr][newc] = 2
                        q.append((newr,newc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

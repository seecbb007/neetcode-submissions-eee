class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        def backtrack(r,c,index):
            if index == len(word):
                return True

            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]):
                return False
            temp = board[r][c]
            board[r][c] = "*"

            for dr,dc in directions:
                newr = dr + r
                newc = dc + c

                if backtrack(newr,newc,index + 1):
                    return True

            board[r][c] = temp
            return False

        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True

        return False
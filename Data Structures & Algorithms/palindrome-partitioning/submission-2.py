class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # "abba"
        res = []
        path = []
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i,n):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

        def backtrack(start):
            if start == n:
                res.append(list(path))
                return

            for i in range(start, n):
                if dp[start][i]:
                    path.append(s[start: i + 1])
                    backtrack(i + 1)
                    path.pop()

        backtrack(0)
        return res 


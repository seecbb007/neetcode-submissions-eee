class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_palindrome(s):
            l,r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l +=1
                r -= 1
            return True

        def backtrack(start):
            if start == len(s):
                res.append(list(path))
                return

            for i in range(start, len(s)):
                substring = s[start: i + 1]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(i + 1)
                    path.pop()

        backtrack(0)
        return res

        
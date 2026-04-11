class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        
        def extend_count(l,r):
            res = 0
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res
        
        for i in range(n):
            count += extend_count(i,i)
            count += extend_count(i,i + 1)
        return count
        
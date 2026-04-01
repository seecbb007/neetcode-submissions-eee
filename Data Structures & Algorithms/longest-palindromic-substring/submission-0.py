class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0

        def palindrome(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        for i in range(len(s)):
            # 奇数
            l1, r1 = palindrome(i, i)
            # 偶数
            l2, r2 = palindrome(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end+1]
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sset = set()
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in sset:
                sset.remove(s[left])
                left += 1
            
            sset.add(s[right])
            res = max(res, right - left + 1)
        return res 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        l, res = 0, 0

        for r,char in enumerate(s):
            count[char] += 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(r - l + 1, res)
        return res

        
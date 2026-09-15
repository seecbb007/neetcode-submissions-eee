class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        mostcommon = 0
        left = 0
        res = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right],0) + 1
            mostcommon = max(mostcommon,counts[s[right]])

            while (right - left + 1) > k + mostcommon:
                counts[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res

        
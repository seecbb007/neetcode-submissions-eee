class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        res = 0
        maxfreq = 0

        for right in range(len(s)):
            char_right = s[right]
            count[char_right] += 1
            maxfreq = max(maxfreq, count[char_right])

            if (right - left + 1) - maxfreq > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1 )
        return res 

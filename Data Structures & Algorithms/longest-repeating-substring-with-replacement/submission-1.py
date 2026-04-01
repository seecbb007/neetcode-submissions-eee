class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        res = 0
        left = 0 
        maxfreq = 0

        for right, char in enumerate(s):
            idx = ord(char) - ord('A')
            count[idx] += 1
            maxfreq = max(maxfreq, count[idx])    

            while (right - left + 1) - maxfreq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            res = max(res, right - left + 1)    
        return res 

 


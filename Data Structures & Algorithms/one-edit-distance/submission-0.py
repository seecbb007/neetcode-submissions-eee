class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        lens,lent = len(s), len(t)
        if abs(lens - lent) > 1:
            return False
        i = j = 0
        count = 0
        while i < lens or j < lent:
            if i < lens and j < lent and s[i] == t[j]:
                i += 1
                j += 1
            else:
                count += 1
                if count > 1:
                    return False
                
                if lens == lent:
                    i += 1
                    j += 1
                elif lens < lent:
                    j += 1
                else:
                    i += 1
        return count == 1

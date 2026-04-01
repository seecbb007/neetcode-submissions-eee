class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts1 = [0] * 26
        windowcount = [0] * 26

        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord('a')] += 1
            windowcount[ord(s2[i]) - ord('a')] += 1

        if counts1 == windowcount:
            return True

        left = 0 
        for right in range(len(s1),len(s2)):
            windowcount[ord(s2[right]) - ord('a')] += 1
            windowcount[ord(s2[left]) - ord('a')] -= 1
            left += 1
            
            if counts1 == windowcount:
                return True
        return False






s1 = "ab"
s2 = "eidbaooo"
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = Counter(s1)
        counts2 = {}
        left = 0
        if len(s1) > len(s2):
            return False

        for right in range(len(s2)):
            
            counts2[s2[right]] = counts2.get(s2[right],0) + 1

            if right - left + 1 > len(s1):
                counts2[s2[left]] -= 1
                if counts2[s2[left]] == 0:
                    del counts2[s2[left]]
                left += 1
            if counts2 == counts1:
                return True
        return False
        

        
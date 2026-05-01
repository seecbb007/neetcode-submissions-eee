class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = Counter(s)
        countt = Counter(t)
        return counts == countt

        
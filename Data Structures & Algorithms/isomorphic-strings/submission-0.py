class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s2t = {}
        t2s = {}

        for chars,chart in zip(s,t):
            if chars in s2t and s2t[chars] != chart:
                return False
            if chart in t2s and t2s[chart] != chars:
                return False

            s2t[chars] = chart
            t2s[chart] = chars
        return True

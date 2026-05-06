class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        currshift = 0
        n = len(s)
        for direc, amount in shift:
            if direc == 0:
                currshift -= amount
            else:
                currshift += amount
        final = currshift % n
        return s[n - final:] + s[:n - final]
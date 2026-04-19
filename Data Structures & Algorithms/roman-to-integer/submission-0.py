class Solution:
    def romanToInt(self, s: str) -> int:
        chart = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        n = len(s)
        total = 0
        for i in range(n):
            if i < n - 1 and chart[s[i]] < chart[s[i + 1]]:
                total -= chart[s[i]]
            else:
                total += chart[s[i]]
        return total
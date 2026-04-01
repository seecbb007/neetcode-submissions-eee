class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        needcount = len(need)
        window = defaultdict(int)

        have = 0
        res = [-1,-1]
        reslen = float("inf")
        left = 0

        for right, char in enumerate(s):
            window[char] += 1
            if char in need and window[char] == need[char]:
                have += 1
            while have == needcount:
                if (right - left + 1) < reslen:
                    res = [left, right]
                    reslen = right - left + 1

                leftchar = s[left]
                window[leftchar] -= 1

                if leftchar in need and window[leftchar] < need[leftchar]:
                    have -= 1
                left += 1
        l,r = res
        return s[l: r + 1] if reslen != float("inf") else ""


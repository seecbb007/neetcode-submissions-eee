class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)
        have, requierd = 0, len(need)
        best_len, best_l = float('inf'), 0
        l = 0

        for r, char in enumerate(s):
            window[char] += 1
            if char in need and window[char] == need[char]:
                have += 1

            while have == requierd:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l

                left_char = s[l]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                l += 1                   
        return "" if best_len == float('inf') else s[best_l: best_len + best_l]




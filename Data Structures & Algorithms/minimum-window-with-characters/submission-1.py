class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)
        have,required = 0, len(need)

        best_len = float('inf')
        best_l = 0
        l = 0

        for r, char in enumerate(s):
            window[char] += 1
            if char in need and window[char] == need[char]:
                have += 1

            while have == required:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l

                left_c = s[l]
                window[left_c] -= 1
                if left_c in need and window[left_c] < need[left_c]:
                    have -= 1

                l += 1

        return "" if best_len == float('inf') else s[best_l : best_l + best_len]

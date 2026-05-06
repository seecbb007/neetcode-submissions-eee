class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        odd_count = 0
        for freq in count.values():
            if freq % 2 != 0:
                odd_count += 1

        return odd_count <= 1

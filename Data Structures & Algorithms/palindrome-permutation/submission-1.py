class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        record = 0
        for freq in count.values():
            if freq % 2 != 0:
                record += 1

        return record <= 1
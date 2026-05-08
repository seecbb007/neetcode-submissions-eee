class Solution:
    def maxDifference(self, s: str) -> int:

        count = Counter(s)
        oddmax = float('-inf')
        evenmax = float('inf')
        for freq in count.values():
            if freq % 2 != 0:
                oddmax = max(oddmax, freq)
                print(oddmax)
            else:
                evenmax = min(evenmax, freq)
                print(evenmax)
        return oddmax - evenmax

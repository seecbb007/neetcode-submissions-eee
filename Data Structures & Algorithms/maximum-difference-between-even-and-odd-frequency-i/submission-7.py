class Solution:
    def maxDifference(self, s: str) -> int:

        count = Counter(s)
        max_odd_freq = float('-inf')
        min_even_freq = float('inf')
        for freq in count.values():
            if freq % 2 != 0:
                max_odd_freq = max(max_odd_freq, freq)
                
            else:
                min_even_freq = min(min_even_freq, freq)
               
        return max_odd_freq - min_even_freq

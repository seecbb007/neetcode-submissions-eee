class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1;
            else:
                freq[num] = 1    

        sortElement = sorted(freq, key = freq.get, reverse = True) 
        return sortElement[:k]     
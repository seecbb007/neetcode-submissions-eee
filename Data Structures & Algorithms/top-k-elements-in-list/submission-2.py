class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        COUNT = Counter(nums)
        sorted_items = sorted(COUNT.items(), key = lambda x : x[1],reverse = True)
        return [num for num, freq in sorted_items[:k]]

        
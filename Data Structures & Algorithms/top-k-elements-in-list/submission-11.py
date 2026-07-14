class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        minheap = []
        for num, freq in count.items():
            heapq.heappush(minheap, (freq, num))
            if len(minheap) > k:
                heapq.heappop(minheap)

        res = []
        while minheap:
            freq,num = heapq.heappop(minheap)
            res.append(num)
        return res 
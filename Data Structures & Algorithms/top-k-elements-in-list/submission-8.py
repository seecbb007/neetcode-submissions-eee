class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        for val, freq in count.items():
            buckets[freq].append(val)

        res = []
        for i in range(len(buckets) - 1, -1 ,-1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res


        
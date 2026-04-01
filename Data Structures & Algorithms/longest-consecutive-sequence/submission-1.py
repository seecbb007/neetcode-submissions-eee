class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in numset:
                length = 1
                while num + length in numset:
                    length += 1
                res = max(res, length)
        return res 
        